from django.http import Http404
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import viewsets


from school.models import School, Student
from rest_framework.decorators import action

from school.serializer import SchoolSerializer, StudentSerializer


class StudentViewSet(viewsets.ViewSet):
    """
    CRUD operation for students.
    """
    serializer_class = StudentSerializer
    
    @action(detail=False, methods=['get'])
    def get_all(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    @action(detail=True, methods=['get'])
    def get_students(self, request, pk=None):
        student = Student.objects.filter(id=pk).last()
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=200)

    @action(detail=False, methods=['post'])
    def create_student(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            first_name = serializer.data['first_name']
            last_name = serializer.data['last_name']
            school = School.objects.filter(
                name=serializer.data['school_name']).last()
            if not school:
                Response(
                    {"message": "No Matching school name, Please add school first."}, status=400)
            Student.objects.create(first_name=first_name,
                                   last_name=last_name, school=school)
            return Response({'status': 'Student created successfully'}, status=200)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SchoolViewSet(viewsets.ViewSet):
    """
    CRUD operation for school.
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    @action(detail=True, methods=['get'])
    def get_school(self, request, pk=None):
        school = School.objects.filter(id=pk).last()

        if not school:
            return Response({"message": "Invalid school id"}, status=400)

        serializer = SchoolSerializer(school)
        return Response(serializer.data, status=200)

    @action(detail=False, methods=['post'])
    def create_school(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            School.objects.create(name=serializer.data['name'])
            return Response({'status': 'School created successfully'}, status=200)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
