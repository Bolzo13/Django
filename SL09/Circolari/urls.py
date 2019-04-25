from django.urls import path

from . import views

urlpatterns = [
    #ex: /Circolari
    path('', views.index, name='index'),
    # ex: /Circolari/5/
    path('<int:circolare_id>/', views.detail, name='detail'),
]