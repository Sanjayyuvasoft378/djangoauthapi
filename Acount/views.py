from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth import authenticate
from Acount.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegistrationAPI(APIView):
    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            users = serializer.save()
            token = get_tokens_for_user(users)
            return Response({"token": token, "msg": "Registration successfully"}, 
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPI(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({"token": token, "msg": "Login Success"},
                                status=status.HTTP_200_OK)
            else:
                return Response({"error": {"non_field_errors": 
                    ['email or password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyProfileViewAPI(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, formate=None):
        Serializer = MyProfileViewSerializer(request.user)
        return Response(Serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordAPI(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data,
                                                  context={'user': request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({"msg": "Password change Successfully"}, 
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, 
                        
                        status=status.HTTP_400_BAD_REQUEST)


class SandPasswordEmailAPI(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = SendEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({"msg": "link sent successfully"}, 
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, 
                        status=status.HTTP_400_BAD_REQUEST)


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token,  format=None):
        serializer = userPasswordResetSerializer(data=request.data)
        context = {"uid": uid, 'token': token}
        if serializer.is_valid(raise_exception=True):
            return Response({"msg": "password reset successfully"}, 
                            status=status.HTTP_200_OK)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class MaincategoryAPI(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        try:
            Serializer = MainCatgorySerializer(data=request.data)
            if Serializer.is_valid(raise_exception=True):
                Serializer.save()
                return Response({"msg": "Data Added successfully"},
                                status=status.HTTP_201_CREATED)
            return Response(Serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"msg": "Internal server error {}".format(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, format=None):
        try:
            get_data = MainCategory.objects.all()
            Serializer = MainCatgorySerializer(get_data, many=True)
            return Response(Serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"msg": "Internal server error {}".format(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def delete(self, request,id,format=None):
        try:
            id = request.GET.get('id')
            get_data = MainCategory.object.filter(id=id).delete()
            MainCatgorySerializer(get_data,many=True)
            return Response({"msg":"Data deleted successfully"},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"msg":"Internal server error {}".format(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
class SubCategoryAPI(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request,format=None):
        try:
            Serializer = SubCatgorySerializer(data = request.data)
            if Serializer.is_valid():
                Serializer.save()
                return Response({"msg":"Data added successfully"},
                                status=status.HTTP_201_CREATED)
            return Response(Serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"msg":"Internal server error {}".format(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, format=None):
        try:
            get_data = SubCategory.objects.all()
            
            Serializer = SubCatgorySerializer(get_data, many=True)        
            return Response(Serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"msg":"Internal server error {}".format(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def delete(self, request, format=None):
        try:
            id = request.GET.get('id')
            get_data = SubCategory.objects.filter(id=id).delete()
            SubCatgorySerializer(get_data,many=True)
            return Response({"msg":"Data deleted successfully"},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"msg":"Internal server error {}".format(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
class ChildCategoryAPI(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request,format=None):
        try:
            Serializer = ChildCategorySerializer(data = request.data)
            if Serializer.is_valid():
                Serializer.save()
                return Response({"msg":"Data added successfully"},
                                status=status.HTTP_201_CREATED)
            return Response(Serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"msg":"Internal server error {}".format(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, format=None):
        try:
            get_data = ChildCategory.objects.all()
            Serializer = ChildCategorySerializer(get_data, many=True)        
            return Response(Serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"msg":"Internal server error {}".format(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def delete(self, request, format=None):
        try:
            id = request.GET.get('id')
            get_data = ChildCategory.objects.filter(id=id).delete()
            ChildCategorySerializer(get_data,many=True)
            return Response({"msg":"Data deleted successfully"},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"msg":"Internal server error {}".format(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
