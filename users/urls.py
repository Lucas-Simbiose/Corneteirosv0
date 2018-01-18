# users/urls.py
from django.urls import path
from . import views
from django.conf.urls import url
from . import views as core_views

urlpatterns = [
    url(r'^signup/$', core_views.signup, name='signup'),
    path('perfil/', views.profile, name='perfil'),
    path('dados_time/', views.teamdata, name='dados_time'),
    path('escudo_time/', views.teamcrest, name='escudo_time'),
    path('camisa_time/', views.teamshirt, name='camisa_time'),
    path('torneios_usuario/', views.usertournament, name='torneios_usuario'),
]

# urlpatterns = [
#     path('signup/', views.SignUp.as_view(), name='signup'),
# ]