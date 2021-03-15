from django.urls import path
from django.contrib.auth import views as authViews
from . import views


urlpatterns = [
    # path('', views.home, name='home'),
    path('', authViews.LoginView.as_view(template_name='user/user.html'), name='home'),
    path('about', views.about, name='about'),
]
