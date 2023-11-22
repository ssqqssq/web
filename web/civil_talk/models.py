from django.db import models
from django.contrib.auth.models import User


class Articles(models.Model):
    title_talk = models.CharField('Тема обращения', max_length=75)
    full_text = models.TextField('Обращение')
    date = models.DateTimeField('Дата', auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_talk

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'





