from datetime import datetime, timedelta

import requests
from celery import shared_task
from django.utils.timezone import now

from config import settings
from users.models import User


class CheckLastVisitMiddleware(object):
    def process_response(self, request, response):
        if request.user.is_authenticated():
            User.objects.filter(pk=request.user.pk).update(last_visit=now())
        return response


@shared_task
def sending_notification(list_id):
    for item_id in list_id:
        requests.post(
            url=f'{settings.URL_FOR_TELEGRAM}{settings.TELEGRAM_BOT_TOKEN}/sendMessage',
            data={
                'chat_id': item_id,
                'text': 'В ваш курс внесены изменения. Зайдите на сайт!'

            }

        )


@shared_task(name='checking_users_activity')
def checking_users_activity():
    print('Check Function')
    max_inactive_period = (datetime.today() - timedelta(30)).date()
    users = User.objects.all()
    for user in users:
        if user.last_login:
            last_activity = user.last_login.date()
            if last_activity < max_inactive_period:
                user.is_active = False
                user.save()

