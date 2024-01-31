from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from studies.models import Course
from studies.paginators.course import CoursePaginator
from studies.permissions import IsModerator, IsOwner
from studies.serializers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    # def get_permissions(self):
    #     if self.action == 'create':
    #         permission_classes = [IsAuthenticated, ~IsModerator]
    #     elif self.action == 'retrieve' or self.action == 'list' or self.action == 'update':
    #         permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    #     elif self.action == 'destroy':
    #         permission_classes = [IsAuthenticated & IsOwner]
    #
    #     return [permission() for permission in permission_classes]

    # def get_queryset(self):
    #     # Если пользователь модератор, выводим все курсы
    #     if self.request.user.is_staff:
    #         return Course.objects.all()
    #     # Иначе фильтруем по принадлежности автору
    #     else:
    #         id_author = self.request.user
    #         return Course.objects.filter(course_author=id_author)
