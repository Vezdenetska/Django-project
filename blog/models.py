from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class News(models.Model):
    title = models.CharField('Tytuł artykułu', max_length=100, unique=True)
    text = models.TextField('Tekst artykułu')
    date = models.DateTimeField('Data:', default=timezone.now)
    avtor = models.ForeignKey(User, verbose_name='Autor:', on_delete=models.CASCADE)

    views = models.IntegerField('Wyświetlenia:', default=1)

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Wiadomość'
        verbose_name_plural = 'Wiadomości'