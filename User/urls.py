from django.urls import path

from . import views

urlpatterns = [
    path('Signup/', views.Signup),
	path('ID_Check/', views.ID_Check),
	path('signup_process/', views.signup_process),
	path('test/', views.Encoding_test),
	path('Login/',views.Login),
	path('login_process/', views.login_process),
	path('logout_process/', views.logout_process),

]