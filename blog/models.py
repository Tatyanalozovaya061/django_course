from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='название блога')
    slug = models.CharField(max_length=200, **NULLABLE, verbose_name='slug')
    content = models.TextField(**NULLABLE, verbose_name='содержимое блога')
    image = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='изображение')
    date_created = models.DateField(**NULLABLE, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликован')
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
