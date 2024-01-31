from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from studies.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.course = Course.objects.create(
            title='test_course1',
            description='description test_course1'
        )

        self.lesson = Lesson.objects.create(
            title="test_lesson1",
            description="description test_lesson1",
            from_course=self.course
        )

    def test_lesson_list(self):
        """Тест вывода списка уроков"""
        response = self.client.get(
            reverse('studies:lesson-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'id': self.lesson.id,
                        'link_to_video': None,
                        'title': 'test_lesson1',
                        'description': 'description test_lesson1',
                        'preview': None,
                        'from_course': self.course.id,
                        'lesson_author': None
                    }
                ]
            }
        )

    def test_create_lesson(self):
        """Тест на создание урока"""
        data = {
            "title": "test_lesson2",
            "description": "description test_lesson2",
            "from_course": self.course.pk,
            "link_to_video": "test_link"
        }

        response = self.client.post(
            reverse('studies:lesson-create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_create_invalid_lesson(self):
        """Тест на создание урока с невалидной ссылкой на видео"""
        data = {
            "title": "test_lesson2",
            "description": "description test_lesson2",
            "from_course": self.course.pk,
            "link_to_video": "https://www.vk.com/watch?"
        }

        response = self.client.post(
            reverse('studies:lesson-create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.json(),
            {'link_to_video': ['Ссылка указана некорректно или ведёт на сторонний ресурс!']}

        )

    def test_lesson_retrieve(self):
        """Тест на вывод одного урока """

        response = self.client.get(
            reverse('studies:lesson-retrieve', kwargs={'pk': self.lesson.id})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_lesson_update(self):
        """Тест на редактирование экземпляра урока"""
        data = {
            "title": "New update lesson1",
            "description": "News description"
        }

        response = self.client.patch(
            reverse('studies:lesson-update', kwargs={'pk': self.lesson.id}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.lesson.refresh_from_db()

        self.assertEqual(
            self.lesson.title,
            data['title']
        )

        self.assertEqual(
            self.lesson.description,
            data['description']
        )

    def test_delete_lesson(self):
        """Тест на удаление урока"""

        response = self.client.delete(
            reverse('studies:lesson-delete', kwargs={'pk': self.lesson.id})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.course = Course.objects.create(
            title='test_course',
            description=' description test_course'
        )

        self.user = User.objects.create(
            email='ivanov@mail.ru',
            is_active=True
        )

        self.user.set_password('09876')
        self.user.save()

    def test_subscription_create(self):
        """Тестирование создание подписки"""

        data = {
            "user": self.user.pk,
            "course": self.course.pk
        }

        response = self.client.post(
            reverse('studies:subscription-create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_subscription_delete(self):
        """Тест удаления подписки"""
        course = Subscription.objects.create(
            user=self.user,
            course=self.course
        )

        response = self.client.delete(
            reverse('studies:subscription-delete', kwargs={'pk': course.pk})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
