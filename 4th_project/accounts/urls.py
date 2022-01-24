from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('', views.dashboard,name='dashboard'),
    path('user/', views.userPage, name="user-page"),
    path('products/', views.products,name='products'),
    path('account/', views.accountSettings, name="account"),
    path('customer/<int:pk>/', views.customer,name='customer'),
    path('create_order/', views.createOrder,name='create_order'),
    # path('create_order/<int:pk>/', views.createOrder,name='create_orders'),
    path('update_order/<int:pk>/', views.updateOrder,name='update_order'),
    path('delete_order/<int:pk>/', views.deleteOrder,name='delete_order'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),
]


'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''