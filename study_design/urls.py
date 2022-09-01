from django.urls import path

from . import views

app_name = 'study_design'
urlpatterns = [
    path('', views.study_design, name='study_design'),
]
