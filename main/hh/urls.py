from django.urls import path

from hh import views

urlpatterns = [
    path('', views.vacancy_list, name='vacancy_list'),
    path('vacancy/<int:id>/', views.vacancy_detail, name='vacancy_detail'),
    path('vacancy/<int:vacancy_id>/resume/create/', views.resume_create, name='resume_create'),
]
