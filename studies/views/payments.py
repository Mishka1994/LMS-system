import stripe
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from config import settings
from studies.models import Payments, Course
from studies.serializers.payments import PaymentSerializer


class PaymentsViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson',)
    ordering_fields = ['date_of_payment', 'payment_method']
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # API-ключ для работы с StripeAPI
        stripe.api_key = settings.STRIPE_API_KEY
        # Получаем id цены указанного в запросе продукта
        object_price_id = settings.LIST_PRODUCT_ID[request.data['course']]['price_id']
        # Создаем сессию для оплаты
        object_session = stripe.checkout.Session.create(
            success_url="https://example.com/success",
            line_items=[{"price": f"{object_price_id}", "quantity": 1}],
            mode="payment",
            currency='rub'
        )
        # Создаем экземпляр оплаты
        Payments.objects.create(
            course=Course.objects.get(id=request.data['course']),
            user=self.request.user,
            payment_amount=object_session.amount_total,
            session_id=object_session.id,

        )
        content = {
            'message': f'Сессия на оплату создана! '
                       f'Для подтверждения оплаты вызовите RETRIEVE объекта Payments c номером id'
                       f' {Payments.objects.get(session_id=object_session.id).id}',
            'ссылка для перехода к оплате': object_session.url}
        return Response(content)

    def retrieve(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_API_KEY
        object_payment = Payments.objects.get(id=self.kwargs['pk'])
        # id платежной сессии для получения информации о платеже
        objects_session_id = object_payment.session_id
        # Получаем объект сессии
        response = stripe.checkout.Session.retrieve(
            objects_session_id
        )

        if response.payment_status == 'paid':
            answer = "Оплата  прошла",
            object_payment.is_paid = True
            object_payment.save()
            status = response.status
            content = {'answer': answer, 'status': status}

        else:
            answer = "Оплата не прошла"
            url = response.url
            status = response.status
            content = {'answer': answer, 'status': status, 'ссылка для оплаты': url}

        return Response(content)
