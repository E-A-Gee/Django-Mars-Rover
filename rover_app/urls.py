from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index-view'),
    path('results/', views.results, name='results-view'),
    path('<photo_date>/<photo_id>', views.photo, name='photo-view'),
    path('meet_the_rovers/', views.meet, name='meet-view'),
    path('about/', views.about, name='about-view'),
]