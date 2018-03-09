from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^user/$', views.user_redirect, name='user_redirect'),
    url(r'^user/(?P<username>[\w\-]+)/$', views.user_profile, name='user_profile'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
]
