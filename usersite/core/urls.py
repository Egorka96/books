from django.conf.urls import url
from django.contrib.auth.views import login, logout_then_login

from . import views

urlpatterns = [
    url(r'^$', views.book_list),
    url(r'^login/$', login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, {'login_url': '/login/'}, name='login'),
]
