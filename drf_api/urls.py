from django.urls import path,include

from rest_framework import routers
from drf_api.views import CourceInfoViewSet, StudentViewSet,FacultyViewSet,SubjectViewSet

router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)
router.register(r'cource_info', CourceInfoViewSet)
router.register(r'faculty', FacultyViewSet)
router.register(r'subject', SubjectViewSet)



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
]