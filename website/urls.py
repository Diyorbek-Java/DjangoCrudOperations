from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name = 'home'),
    path('logout/',views.logout_user, name = 'logout'),
    path('register/',views.register_user,name="register"),
    path('record/<int:pk>',views.custom_record,name="record")
]
