from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path("<int:day>",views.Challange_by_no,),
    path("<str:day>",views.Challange_by_name,name="week-challange"),
    ]