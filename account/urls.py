from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
import shop.views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', shop.views.product_list, name='product_list'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),

]
