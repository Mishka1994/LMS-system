from rest_framework import serializers

from studies.models import Lesson


class LessonCountSerializer(serializers.ModelSerializer):
    lesson_number = serializers.SerializerMethodField()

    def get_lesson_number(self, obj):
        return obj.title.all().count()

    class Meta:
        model = Lesson
        fields = ('lesson_number',)


class LessonOfCourse(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()

    def get_lessons(self, obj):
        return None
    class Meta:
        model = Lesson
        fields = ('lessons',)


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
