from Acount.views import ChildCategoryAPI, EditProfileAPI, MaincategoryAPI, MyProfileViewAPI, RegistrationAPI, SandPasswordEmailAPI, SubCategoryAPI, UserChangePasswordAPI, UserLoginAPI, UserPasswordResetView
from django.urls import path
urlpatterns = [

path('register/',RegistrationAPI.as_view(),name='RegistrationAPI'),
path('login/',UserLoginAPI.as_view(),name='UserLoginAPI'),
path('profileview/',MyProfileViewAPI.as_view(),name='myprofileview'),
path('changePassword/',UserChangePasswordAPI.as_view(),name='UserChangePasswordAPI'),
path('SandPasswordEmailAPI/',SandPasswordEmailAPI.as_view(),name='SandPasswordEmailAPI'),
path('passwordreset/<uid>/<token>/', UserPasswordResetView.as_view(),name='UserPasswordResetView'),
path('editprofile/',EditProfileAPI.as_view(),name='editprofile'),
 
path('maincategory/',MaincategoryAPI.as_view(),name='maincategory'),
path('subcategory/',SubCategoryAPI.as_view(),name='subcategory'),
path('childcategory/',ChildCategoryAPI.as_view(),name='childcategory'),
]