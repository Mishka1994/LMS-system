from django.contrib import admin

from studies.models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'subscription_status',)
    list_filter = ('subscription_status',)

