"""
URL configuration for projecttracker project.

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

# projecttracker/urls.py
# projecttracker/urls.py
# projecttracker/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tracker.views import TaskViewSet, SignupView, LoginView, logout_view, ApiRootView ,data_all # Update import path

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', ApiRootView.as_view(), name='api-root'),
    path('api/', include(router.urls)),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', logout_view, name='logout'),
    path('api/data_all/', data_all, name='data_all'), 
]
