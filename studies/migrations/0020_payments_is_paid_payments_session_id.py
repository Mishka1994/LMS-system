# Generated by Django 5.0.1 on 2024-02-02 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0019_course_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Статус оплаты'),
        ),
        migrations.AddField(
            model_name='payments',
            name='session_id',
            field=models.TextField(blank=True, null=True, verbose_name='Идентификатор сессии'),
        ),
    ]
