# Generated by Django 5.0.1 on 2024-02-02 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0018_alter_lesson_from_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='amount',
            field=models.PositiveIntegerField(default=100, verbose_name='стоимость'),
        ),
    ]