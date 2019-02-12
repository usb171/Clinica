from django.urls import path
from .views import login, dashboard, logout
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', login, name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard', dashboard, name='dashboard'),

    path('senha/resgatar/',
         auth_views.PasswordResetView.as_view(template_name='core/password_reset.html'),
         name='password_reset'),

    path('senha/envio/',
         auth_views.PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'),
         name='password_reset_done'),

    path('senha/resgatar/novaSenha/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='core/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('senha/resgatar/confirmacao/',
         auth_views.PasswordResetView.as_view(template_name='core/password_reset_complete.html'),
         name='password_reset_complete'),

]