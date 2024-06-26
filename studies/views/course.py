from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from studies.models import Course, Subscription
from studies.paginators.course import CoursePaginator
from studies.permissions import IsModerator, IsOwner
from studies.serializers.course import CourseSerializer
from studies.tasks import sending_notification


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action == 'retrieve' or self.action == 'list' or self.action == 'update':
            permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated & IsOwner]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        # Если пользователь модератор, выводим все курсы
        if self.request.user.is_staff:
            return Course.objects.all()
        # Иначе фильтруем по принадлежности автору
        else:
            id_author = self.request.user
            return Course.objects.filter(course_author=id_author)

    def update(self, request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs['pk'])

        list_of_subscription_users = Subscription.objects.filter(course=course)
        list_users_telegram_id = [item.user.telegram_id for item in list_of_subscription_users if item.user.telegram_id]
        sending_notification(list_id=list_users_telegram_id)

        return Response({'result': 'Изменения внесены'})
