from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.user_register, name="user_register"),
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^logout/$', views.user_logout, name="user_logout"),

    url(r'^user/$', views.user_redirect, name='user_redirect'),
    url(r'^user/(?P<username>[\w\-]+)/$', views.user_profile, name='user_profile'),
    url(r'^user/(?P<username>[\w\-]+)/timeline/$', views.user_timeline, name='user_timeline'),
    url(r'^user/(?P<username>[\w\-]+)/groups/$', views.user_groups, name='user_groups'),

    url(r'^group/(?P<group_id>[\w\-]+)/$', views.group_profile, name='group_profile'),
    url(r'^group/(?P<group_id>[\w\-]+)/leaderboards/$', views.group_leaderboards_index, name='group_leaderboards_index'),
    url(r'^group/(?P<group_id>[\w\-]+)/leaderboards/(?P<workout_id>[\w\-]+)/$', views.group_leaderboards_workout, name='group_leaderboards_workout'),
    url(r'^group/(?P<group_id>[\w\-]+)/member_list/$', views.group_member_list, name='group_member_list'),
    url(r'^add_group/', views.add_group, name='add_group'),

    url(r'^leaderboards/$', views.leaderboards_index, name="leaderboards_index"),
    url(r'^leaderboards/(?P<workout_id>[\w\-]+)/$', views.leaderboards_single, name="leaderboards_single"),
]
