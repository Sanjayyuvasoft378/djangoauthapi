from Acount.views import MyProfileViewAPI, RegistrationAPI, UserChangePasswordAPI, UserLoginAPI
from django.urls import path
urlpatterns = [

path('register/',RegistrationAPI.as_view(),name='RegistrationAPI'),
path('login/',UserLoginAPI.as_view(),name='UserLoginAPI'),
path('profileview/',MyProfileViewAPI.as_view(),name='myprofileview'),
path('changePassword/',UserChangePasswordAPI.as_view(),name='UserChangePasswordAPI'),
]