from django.conf.urls import url
from django.contrib.auth import views
from django.urls import path

from Accounts.views import index, signup

urlpatterns = [
    url('^$', view=index),
    url('signup', view=signup, name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
