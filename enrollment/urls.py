from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnrollmentViewSet,StudentEnrollmentsView,CourseResultViewSet

router = DefaultRouter()
router.register('list', EnrollmentViewSet)
router.register('course-results', CourseResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('my-enrollments/', StudentEnrollmentsView.as_view(), name='student-enrollments'),
]