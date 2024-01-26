from rest_framework import serializers

from studies.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.IntegerField(source='course.all.count')
    lessons = serializers.SerializerMethodField()

    def get_lessons(self, obj):
        return [[lesson.title, lesson.description]
                for lesson in Lesson.objects.filter(from_course=obj.id)]

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'course_author', 'lesson_count', 'lessons',)
