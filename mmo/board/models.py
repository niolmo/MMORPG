from django.db import models
from django.contrib.auth.models import User


class Ads(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    CAT = (('tanks', 'Танки'),
           ('healers', 'Хилы'),
           ('damage_dealers', 'ДД'),
           ('dealers', 'Торговцы'),
           ('gildmasters', 'Гилдмастеры'),
           ('quest_givers', 'Квестгиверы'),
           ('blacksmiths', 'Кузнецы'),
           ('tanners', 'Кожевники'),
           ('potion_makers', 'Зельевары'),
           ('spell_masters', 'Мастера заклинаний'))
    category = models.CharField(
        max_length=15, choices=CAT, verbose_name='Категория')
    dateCreation = models.DateField(auto_now_add=True, verbose_name='Создано')
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = ("Объявление")
        verbose_name_plural = ("Объявления")

    def __str__(self):
        return self.name


class Response(models.Model):
    player = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Игрок')
    post = models.ForeignKey(
        Ads, on_delete=models.CASCADE, verbose_name='Объявление')
    text = models.TextField(verbose_name='Текст')
    status = models.BooleanField(default=False, verbose_name='Статус')
    dateCreation = models.DateTimeField(
        auto_now_add=True, verbose_name='Создано')
