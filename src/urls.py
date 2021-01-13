from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import ResetPasswordForm, PasswordSetForm

urlpatterns = [
    path('', views.dashboardPage, name='dashboard'),
    path('product/', views.productPage, name='product'),
    path('customer/<str:pk>/', views.customerPage, name='customer'),
    path('order/<str:pk>/', views.orderDetails, name='order_detail'),
    path('product/<str:pk>/', views.updateProduct, name='product_detail'),

    path('user/', views.userPage, name='user'),
    #path('user/create/<str:pk>/', views.userOrderPage, name='user_order'),

    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),

    path('reset_password/', auth_views.PasswordResetView.as_view(form_class=ResetPasswordForm, template_name='settings/reset_password.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='settings/reset_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(form_class=PasswordSetForm, template_name='settings/password_reset_form.html'), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='settings/password_reset_done.html'), name="password_reset_complete"),
]
