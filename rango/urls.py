from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name="about"),
    url(r'^register/$', views.user_register, name="user_register"),
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^logout/$', views.user_logout, name="user_logout"),

    url(r'^user/$', views.user_redirect, name='user_redirect'),
    url(r'^user/(?P<username>[\w\-]+)/$', views.user_profile, name='user_profile'),
    url(r'^user/(?P<username>[\w\-]+)/timeline/$', views.user_timeline, name='user_timeline'),
    url(r'^user/(?P<username>[\w\-]+)/teams/$', views.user_teams, name='user_teams'),

    url(r'^team/(?P<team_id>[\w\-]+)/$', views.team_profile, name='team_profile'),
    url(r'^team/(?P<team_id>[\w\-]+)/leaderboards/$', views.team_leaderboards_index,
        name='team_leaderboards_index'),
    url(r'^team/(?P<team_id>[\w\-]+)/leaderboards/(?P<workout_id>[\w\-]+)/$', views.team_leaderboards_workout,
        name='team_leaderboards_workout'),
    url(r'^team/(?P<team_id>[\w\-]+)/member_list/$', views.team_member_list, name='team_member_list'),
    url(r'^add_team/', views.add_team, name='add_team'),

    url(r'^leaderboards/$', views.leaderboards_index, name="leaderboards_index"),
    url(r'^leaderboards/(?P<workout_id>[\w\-]+)/$', views.leaderboards_single, name="leaderboards_single"),
]
