from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда для создания тестовых пользователей"""
    def handle(self, *args, **options):
        test_users = [
            {'id': 2, 'email': 'test2@mail.ru', 'password': 'qwerty', 'is_staff': True},
            {'id': 3, 'email': 'test3@mail.ru', 'password': 'asdfg', 'is_staff': False}
        ]
        for item in test_users:
            user = User.objects.create(
                id=item['id'],
                email=item['email'],
                is_staff=item['is_staff']
            )
            user.set_password(item['password'])
            user.save()
