from django.urls import path
from . import views

app_name = 'predict'

urlpatterns = [
    path('', views.predict ,name='predict'),
    path('predict/', views.predict_chances, name='submit_prediction'),
    path('results/', views.view_results, name='results'),
    path('visual/', views.view_visual, name='visual'),
    path('boxplot/', views.view_boxplot, name='boxplot'),
]