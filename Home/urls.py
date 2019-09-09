from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
    ## Function view
    #path('', views.Index.as_view(), name='index'),

    # Class-based Views
    path('', views.Index.as_view(), name='index'),
    path('about/', views.About.as_view(), name='about'),
]
