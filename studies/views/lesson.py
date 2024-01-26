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
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated & (IsModerator | IsOwner)]


class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated & (IsModerator & IsOwner)]


class LessonUpdateView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated & (IsModerator | IsOwner)]


class LessonDeleteView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated & IsOwner & ~IsModerator]
