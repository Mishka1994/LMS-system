from rest_framework import viewsets
from rest_framework.response import Response

from studies.models import Course
from studies.serializers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = CourseSerializer(self.queryset, many=True)

        return Response(serializer.data)
