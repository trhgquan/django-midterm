from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('user/', views.user_page, name = 'user-page'),
    path('account/', views.account_page, name = 'account-page'),

    path('products/', views.products, name = 'products'),
    path('customer/<str:customer_id>/', views.customer, name = 'customer'),

    # Authentication
    path('register/', views.register_page, name = 'register'),
    path('login/', views.login_page, name = 'login'),
    path('logout/', views.logout_page, name = 'logout'),

    # Reset password
    path(
        'reset_password/', 
        auth_views.PasswordResetView.as_view(template_name = 'accounts/auth/password_reset.html'),
        name = 'reset_password'
    ),

    path(
        'reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/auth/reset_password_sent.html'),
        name = 'password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name = 'accounts/auth/new_password.html'),
        name = 'password_reset_confirm'
    ),
    path(
        'reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name = 'accounts/auth/password_reset_done.html'),
        name = 'password_reset_complete'
    ),

    # Orders
    path('create_order/<str:customer_id>/', views.create_order, name = 'create_order'),
    path('update_order/<str:order_id>/', views.update_order, name = 'update_order'),
    path('delete_order/<str:order_id>/', views.delete_order, name = 'delete_order'),

]
