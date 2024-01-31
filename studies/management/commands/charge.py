from django.core.management import BaseCommand

from studies.models import Payments, Course, Lesson
from users.models import User


class Command(BaseCommand):
    """Команда для создания тестовых моделей платежей"""
    def handle(self, *args, **options):
        customer_1 = User.objects.get(last_name='Петрова')
        customer_2 = User.objects.get(last_name='Иванов')
        list_of_payments = [
            {'course': Course.objects.get(id=1), 'user': customer_2, 'payment_amount': 30000, 'payment_method': 'TRANSFER'},
            {'lesson': Lesson.objects.get(id=4), 'user': customer_1, 'payment_amount': 1500, 'payment_method': 'CASH'}
        ]

        payments_for_create = []

        for item in list_of_payments:
            payments_for_create.append(
                Payments(**item)
            )

        Payments.objects.bulk_create(payments_for_create)
