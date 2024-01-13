from django.urls import path
from . import views



app_name="AstraDev"
urlpatterns=[
    path("",views.profile, name="profile"),
]

