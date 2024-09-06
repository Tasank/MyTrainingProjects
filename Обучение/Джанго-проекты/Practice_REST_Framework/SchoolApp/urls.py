from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'schools', views.SchoolViewset)
router.register(r'classes', views.SClassViewset)
router.register(r'students', views.StudentViewest)


urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]