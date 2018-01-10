# users/urls.py
from django.urls import path
from . import views
from django.conf.urls import url
from . import views as core_views

urlpatterns = [
    url(r'^signup/$', core_views.signup, name='signup'),
    path('perfil/', views.profile, name='perfil'),
]

# urlpatterns = [
#     path('signup/', views.SignUp.as_view(), name='signup'),
# ]