from asyncore import write
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from xml.dom import ValidationErr
from rest_framework import serializers
from .models import *
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':"password"}
                                      ,write_only=True)
    class Meta:
        model = User
        fields = ['email','password','password2','name','tc']
        extra_kwargs = {
            "password":{"write_only":True}
        }
        
    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("password and confirm_password doesn't match")
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
            
            
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email','password']
        
        
class MyProfileViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','name']
        
class EditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'

class UserChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255,
                                     style={"input_type":"password"},write_only=True)
    password2 = serializers.CharField(max_length=255,
                                      style={"input_type":"password"},write_only=True)
    class Meta:
        model = User
        fields = ['password','password2']

    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError("password and confirm password doesn`t match")
        user.set_password(password)
        user.save()
        return attrs

class SendEmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email']
    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email = email)
            print("333",user)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('222',uid)
            token = PasswordResetTokenGenerator().make_token(user)
            link = 'http://localhost/3000/acount/reset/'+uid+'/'+token
            print("link",link)
            return attrs
        else:
            raise ValidationErr('you are not a register user')
        
        
        
class userPasswordResetSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=255,
                                     style={"input_type":"password"},write_only=True)
    password2 = serializers.CharField(max_length=255,
                                      style={"input_type":"password"},write_only=True)
    class Meta:
        model = User
        fields = ['password','password2']

    def validate(self,attrs):
        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password != password2:
                raise serializers.ValidationError("password and confirm password doesn`t match")
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise ValidationErr("token is not valid or expred")
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user,token)
            raise ValidationErr("token is not valid or expired ")

class MainCatgorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = '__all__'

class SubCatgorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
        
class ChildCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildCategory
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
