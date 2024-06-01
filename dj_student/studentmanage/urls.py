from django.urls import path
from . import views

urlpatterns =[
    path('', views.studenthomepage, name='studenthomepage'),
    path('<int:id>', views.see_student, name='see_student'),
    path('add/', views.add, name='add'),
]