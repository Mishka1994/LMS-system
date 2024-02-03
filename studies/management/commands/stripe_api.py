import stripe
from django.core.management import BaseCommand

from config import settings


class Command(BaseCommand):
    """Команда для создания продуктов и цен на ресурсе Stripe API"""
    def handle(self, *args, **options):
        stripe.api_key = settings.STRIPE_API_KEY

        course_1 = stripe.Product.create(
            name="Course №1(Курс по ЯП С/C++)",
            description="subscription",
        )

        price_for_course1 = stripe.Price.create(
            unit_amount=10000,
            currency="rub",
            product=course_1["id"],
        )

        course_2 = stripe.Product.create(
            name="Course №2(Курс Структуры данных)",
            description="subscription"
        )

        price_for_course2 = stripe.Price.create(
            unit_amount=8000,
            currency="rub",
            product=course_2["id"],
        )

        course_3 = stripe.Product.create(
            name="Course №3(Курс Алгоритмы и структуры данных на Python)",
            description="subscription",
        )

        price_for_course3 = stripe.Price.create(
            unit_amount=6000,
            currency="rub",
            product=course_3["id"],
        )
        print(f'1 курс_id {course_1.id}, цена_id - {price_for_course1.id}')
        print(f'1 курс_id {course_2.id}, цена_id - {price_for_course2.id}')
        print(f'1 курс_id {course_3.id}, цена_id - {price_for_course3.id}')

