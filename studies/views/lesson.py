from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from studies.models import Lesson
from studies.permissions import IsModerator, IsOwner
from studies.serializers.lesson import LessonSerializer


class LessonCreateView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated & ~IsModerator]


class LessonRetrieveView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    # queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Lesson.objects.all()
        else:
            author_id = self.request.user
            return Lesson.objects.filter(lesson_author=author_id)


class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    # queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Lesson.objects.all()
        else:
            author_id = self.request.user
            return Lesson.objects.filter(lesson_author=author_id)


class LessonUpdateView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDeleteView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated & IsOwner & ~IsModerator]
