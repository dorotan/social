from django.conf.urls import url
from . import views

urlpatterns = [
	#Widok logowania
	url(r'^login/$', views.user_login, name='login'),
]