# Generated by Django 5.0.1 on 2024-01-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название блога')),
                ('slug', models.CharField(blank=True, max_length=200, null=True, verbose_name='slug')),
                ('content', models.TextField(blank=True, null=True, verbose_name='содержимое блога')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='изображение')),
                ('date_created', models.DateField(verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликован')),
                ('view_count', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]
