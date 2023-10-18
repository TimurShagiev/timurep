"""
URL configuration for problem_list project.

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
from prob_list import views as problems_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prob_list/', problems_views.problem_list, name='problem_list'),
    path('prob_list/<int:problem_id>/', problems_views.problem_detail, name='problem_detail'),
    path('prob_list/create/', problems_views.new_problem, name='new_problem'),
]