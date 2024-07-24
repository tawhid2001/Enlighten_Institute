from django.shortcuts import get_object_or_404
from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Enrollment,CourseResult
from .serializers import EnrollmentSerializer,CourseResultSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    def get_queryset(self):
        student = self.request.user
        return Enrollment.objects.filter(student=student)
    
    def create(self, request, *args, **kwargs):
        student = request.user
        course_id = request.data.get('course')
        if Enrollment.objects.filter(student=student, course_id=course_id).exists():
            return Response({'detail': 'Already enrolled in this course.'}, status=status.HTTP_400_BAD_REQUEST)
        data = {'student': student.id, 'course': course_id}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
    
class StudentEnrollmentsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        student = request.user
        enrollments = Enrollment.objects.filter(student=student)
        serializer = EnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)
    
class CourseResultViewSet(viewsets.ModelViewSet):
    queryset = CourseResult.objects.all()
    serializer_class = CourseResultSerializer

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'teacher':
            return CourseResult.objects.filter(enrollment__course__teacher=user)
        elif user.user_type == 'student':
            return CourseResult.objects.filter(enrollment__student=user)
        return CourseResult.objects.none()