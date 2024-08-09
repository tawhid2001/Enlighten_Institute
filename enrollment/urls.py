from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnrollmentViewSet,StudentEnrollmentsView,CourseResultViewSet,EnrolledStudentsView,EditCourseResultViewSet

router = DefaultRouter()
router.register('list', EnrollmentViewSet)
router.register('course-results', CourseResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('my-enrollments/', StudentEnrollmentsView.as_view(), name='student-enrollments'),
    path('students/<int:course_id>/', EnrolledStudentsView.as_view(), name='enrolled-students'),
    path('edit-course-results/<int:pk>/', EditCourseResultViewSet.as_view({'put': 'update'}), name='edit-course-results'),
]