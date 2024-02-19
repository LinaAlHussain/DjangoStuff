from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("lina",views.lina, name='lina'),
    path("sara",views.sara, name='sara')  
]