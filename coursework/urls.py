from django.contrib import admin
from django.urls import path, include
from user import views as userViews
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('linkcut.urls')),
    path('reg/', userViews.register, name='reg'),
    path('profile/', userViews.profile, name='profile'),
    path('user/', authViews.LoginView.as_view(template_name='user/user.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='user/exit.html'), name='exit'),

    path('pass-reset/', authViews.PasswordResetView.as_view(template_name='user/pass_reset.html'),
    name='pass-reset'),

    path('password_reset_complete/', authViews.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),

    path('password_reset_confirm/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
    name='password_reset_confirm'),

    path('password_reset_done/', authViews.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
    name='password_reset_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)