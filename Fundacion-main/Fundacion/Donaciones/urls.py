from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required

urlpatterns = [
    
    # localhost:8000/add_carrera
    path('add_donacion', views.DonacionCreate.as_view(), name="add_donacion"),

    path('list_donacion', views.DonacionList.as_view(), name="list_donacion"),
]