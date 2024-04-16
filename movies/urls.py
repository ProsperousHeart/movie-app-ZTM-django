from django.urls import path

# from movies.views import index, about
from . import views

urlpatterns = [
    # path('', index, name="home"),
    path('', views.index, name="home"),
    # path('', include(views.index), name="home"),
    # path('about/', about, name="about"),
    path('about/', views.about, name="about"),
]
