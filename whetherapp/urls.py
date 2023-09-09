from django.urls import path
from whetherapp import views

urlpatterns = [
    path('',views.index,name='index')
]
