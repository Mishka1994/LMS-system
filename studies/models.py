from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название курса')
    preview = models.ImageField(upload_to='course/', verbose_name='Превью курса', blank=True, null=True)
    description = models.TextField(verbose_name='Описание курса')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока')
    preview = models.ImageField(upload_to='course/lesson/', verbose_name='Превью урока', blank=True, null=True)
    link_to_video = models.URLField(verbose_name='Ссылка на видео', blank=True, null=True)
    from_course = models.ForeignKey(Course, on_delete=models.PROTECT, verbose_name='ссылка на курс',
                                    related_name='course')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payments(models.Model):
    CASH = 'CASH'
    TRANSFER = 'TRANSFER_TO_ACCOUNT'

    list_of_payment_method = [
        (CASH, 'Наличные'),
        (TRANSFER, ' Перевод на счет')
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок', **NULLABLE)

    #user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    user = models.CharField(max_length=256, verbose_name='Пользователь')
    date_of_payment = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    payment_amount = models.PositiveIntegerField(verbose_name='Сумма оплаты', **NULLABLE)
    payment_method = models.CharField(max_length=100, choices=list_of_payment_method,
                                      verbose_name='Способ оплаты', **NULLABLE)

    def __str__(self):
        return (f'{self.user} ({self.payment_amount}, {self.payment_method}) - /'
                f'{self.lesson if self.lesson else self.course}')

    class Meta:
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'
