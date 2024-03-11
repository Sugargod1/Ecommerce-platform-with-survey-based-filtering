from django.urls import path
from . import views

urlpatterns = [
    path('', views.survey, name='survey'),
    path('survey/', views.survey, name='survey'),  # Make sure to replace 'survey_result' with your actual view function
    path('store/', views.store, name='store'),
]
