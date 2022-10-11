from email.policy import default
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# custom user manager create


class UserManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None, password2=None):
        # Creates and saves a User with the given email, name, tc and password.
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email), name=name, tc=tc,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  name, tc, password=None):
        # Creates and saves a superuser with the given email, name, tc and password.
        user = self.create_user(email, password=password, name=name, tc=tc,)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True)
    name = models.CharField(max_length=250)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'tc']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class MainCategory(models.Model):
    categoryName = models.CharField(max_length=255)
    categoryImage = models.ImageField(upload_to='Ecomm_Images')
    description = models.CharField(max_length=255)
    class Meta:
        db_table = "MainCategory"
    def __str__(self):
        return self.categoryName
        

class SubCategory(models.Model):
    mainCategoryId = models.ForeignKey(MainCategory, on_delete=models.CASCADE,default=123)

    categoryName = models.CharField(max_length=255)
    categoryImage = models.ImageField(upload_to = 'Ecomm_Images')
    description = models.CharField(max_length=255)
    class Meta:
        db_table = 'SubCategory'
    def __str__(self):
        return self.categoryName
        
        
class ChildCategory(models.Model):
    mainCategoryId = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    subCategoryId = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    categoryName = models.CharField(max_length=255)
    categoryImage = models.ImageField(upload_to='Ecomm_images')
    description = models.CharField(max_length=255,default=True)
    class Meta:
        db_table = 'ChildCategory'
    def __str__(self):
        return self.categoryName
    
    
class Product(models.Model):
    mainCategoryId = models.ForeignKey(MainCategory,on_delete=models.CASCADE)
    subCategoryId = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    childCategoryId = models.ForeignKey(ChildCategory, on_delete=models.CASCADE)
    productName = models.CharField(max_length = 255)
    productImage = models.ImageField(upload_to = 'EcommProductImages')
    description = models.CharField(max_length = 255)
    qty = models.IntegerField()
    price = models.IntegerField()
    
    class Meta:
        db_table = 'Product'
    def __str__(self):
        return self.productName
