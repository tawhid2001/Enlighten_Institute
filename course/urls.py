from django.urls import path,include
from .views import CourseList,CourseDetail,CourseProgressView,CourseLessonsWithProgress,LessonProgressViewSet

urlpatterns = [
    path('courselist/', CourseList.as_view(),name="course_list"),
    path('courselist/<int:pk>/', CourseDetail.as_view(),name="course_detail"),
    path('course_progress/<int:course_id>/', CourseProgressView.as_view(), name='course_progress'),
    path('courselessons/<int:pk>/', CourseLessonsWithProgress.as_view(),name="course_lessons_with_progress"),
    path('lessonprogress/',LessonProgressViewSet.as_view({'get': 'list'}),name="lesson-progress"),
]