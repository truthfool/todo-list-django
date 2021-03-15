from . import views
from django.urls import path

urlpatterns = [
    path('',views.ToDoListView,name='index'),
    path('remove/<int:id>/',views.DeleteView,name='remove')
]
