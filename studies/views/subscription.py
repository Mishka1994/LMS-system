from rest_framework import generics

from studies.models import Subscription, Course
from studies.serializers.subscription import SubscriptionSerializer


class SubscriptionCreateView(generics.CreateAPIView):
    """View for create subscription"""
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class SubscriptionDeleteView(generics.DestroyAPIView):
    """View for delete subscription"""
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
