from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from studies.models import Lesson, Subscription, Course
from studies.paginators.lesson import LessonPaginator
from studies.permissions import IsModerator, IsOwner
from studies.serializers.lesson import LessonSerializer
from studies.tasks import sending_notification


class LessonCreateView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]

    # permission_classes = [IsAuthenticated & ~IsModerator]
    def create(self, request, *args, **kwargs):
        course = request.data['from_course']
        list_of_subscription_users = Subscription.objects.filter(course=course)
        list_telegram_id_user = [item.user.telegram_id for item in list_of_subscription_users if item.user.telegram_id]
        sending_notification(list_telegram_id_user)

        return Response({'result': 'Изменения внесены'})


class LessonRetrieveView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    # queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
    pagination_class = LessonPaginator

    # permission_classes = [IsAuthenticated, IsModerator | IsOwner]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Lesson.objects.all()
        else:
            author_id = self.request.user.id
            return Lesson.objects.filter(lesson_author=author_id)

    # def retrieve(self, request, *args, **kwargs):
    #     list_of_subscribed_users = Subscription.objects.filter(
    #         course_id=request.data['from_course']
    #     )
    #     print(list_of_subscribed_users.user)


class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = LessonPaginator
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated, IsModerator | IsOwner]

    # def get_queryset(self):
    #     if self.request.user.is_staff:
    #         return Lesson.objects.all()
    #     else:
    #         author_id = self.request.user
    #         return Lesson.objects.filter(lesson_author=author_id)


class LessonUpdateView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]

    # permission_classes = [IsAuthenticated, IsModerator | IsOwner]

    def update(self, request, *args, **kwargs):
        # Из урока получаем экземпляр курса
        course = Lesson.objects.get(pk=kwargs['pk']).from_course
        # В модели подписки получаем все записи с данным курсом
        list_of_subscribed_users = Subscription.objects.filter(
            course=course
        )
        # Из каждой подписки получаем пользователя и его telegram_id.
        list_user_telegram_id = [item.user.telegram_id for item in list_of_subscribed_users if item.user.telegram_id]

        # Полученный ранее список передаем в функцию для рассылки уведомлений
        sending_notification(list_id=list_user_telegram_id)

        return Response({'message': 'Изменения внесены'})


class LessonDeleteView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated & IsOwner & ~IsModerator]
