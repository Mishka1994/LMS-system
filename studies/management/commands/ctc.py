from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Команда для создания тестовых клиентов"""
        list_of_customer = [

            {'id': 4, 'email': 'ivanov@mail.ru', 'password': '09876', 'first_name': 'Иван', 'last_name': 'Иванов',
             'is_staff': False},
            {'id': 5, 'email': 'petrova@mail.ru', 'password': '67890', 'first_name': 'Анна', 'last_name': 'Петрова',
             'is_staff': False},

        ]

        for item in list_of_customer:
            customer = User.objects.create(
                id=item['id'],
                email=item['email'],
                is_staff=item['is_staff'],
                first_name=item['first_name'],
                last_name=item['last_name']
            )
            customer.set_password(item['password'])
            customer.save()

