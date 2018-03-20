from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth import views
from . import views


urlpatterns = [
	#Custom login view
	# url(r'^login/$', views.user_login, name='login'),
	#Builtin login view
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, name='logout'),
	url(r'^logout_then_login/$', auth_views.logout_then_login, name='logout_then_login'),
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^password_change/$', auth_views.password_change, name='password_change'),
	url(r'^password_change/done/$', auth_views.password_change_done, name='password_change_done'),
	url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
	url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
	url(r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
	url(r'^password_reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),
	url(r'^register/$', views.register, name='register'),
]
