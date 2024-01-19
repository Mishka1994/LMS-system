from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название курса')
    preview = models.ImageField(upload_to='course/', verbose_name='Превью курса')
    description = models.TextField(verbose_name='Описание курса')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока')
    preview = models.ImageField(upload_to='course/lesson/', verbose_name='Превью урока')
    link_to_video = models.URLField(verbose_name='Ссылка на видео')
    from_course = models.ForeignKey(Course, on_delete=models.PROTECT, verbose_name='ссылка на курс')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

