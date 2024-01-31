from rest_framework import serializers

from studies.models import Course, Lesson, Subscription

from studies.validators import LinkValidator


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.IntegerField(source='course.all.count', read_only=True)
    lessons = serializers.SerializerMethodField()
    description = serializers.CharField(validators=[LinkValidator()])
    subscription = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'subscription', 'course_author', 'lesson_count', 'lessons',)

    def get_lessons(self, obj):
        return [[lesson.title, lesson.description]
                for lesson in Lesson.objects.filter(from_course=obj.id)]

    def get_subscription(self, obj):
        request = self.context.get('request')

        if request:
            return Subscription.objects.filter(
                user=request.user.id,
                course=obj,
                subscription_status=True
            ).exists()
        return False
