

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("packages/", views.packages, name="packages"),  # No parameters expected here
    path('booking_page/<str:package_name>/', views.booking_page, name='booking_page'),

]
from django.urls import path
from . import views