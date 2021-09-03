from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index-view'),
    path('results/', views.results, name='results-view'),
    path('<photo_date>/<photo_id>', views.photo, name='photo-view'),
]