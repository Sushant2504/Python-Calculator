"""
URL configuration for mplintegration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from mplinit.views import main
from mplinit import views

from django.conf.urls import include
urlpatterns = [
    path('', views.main, name='main'),
    path('graph', views.graph, name='graph'),
    path('algebra', views.algebra, name='algebra'),
    path('steps', views.steps, name='steps'),
    path('tangent_n_normal', views.tangent_n_normal, name='tangent_n_normal'),
    path('normal_plot', views.normal_plot, name='normal_plot'),
    path('area_curve', views.area_curve, name='area_curve'),
    path('summerizer', views.summerizer, name='summerizer')
]
