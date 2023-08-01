from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("index/", views.index),
    path("create/", views.create_admin),
    path("login/", obtain_auth_token, name="login_user"),
    path("logout/", views.logout),
    path("validate_token/", views.validate_token),
    path("order/", views.create_order),
]
