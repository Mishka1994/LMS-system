from django.core.management import BaseCommand

from studies.models import Payments, Course, Lesson


class Command(BaseCommand):
    def handle(self, *args, **options):
        list_of_payments = [
            {'course': Course.objects.get(id=1), 'user': 'Иванов Иван', 'payment_amount': 30000, 'payment_method': 'TRANSFER'},
            {'lesson': Lesson.objects.get(id=4), 'user': 'Петрова Анна', 'payment_amount': 1500, 'payment_method': 'CASH'}
        ]

        payments_for_create = []

        for item in list_of_payments:
            payments_for_create.append(
                Payments(**item)
            )

        Payments.objects.bulk_create(payments_for_create)
