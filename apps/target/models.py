from django.db import models
from apps.users.models import Profile

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE, 
        related_name= 'user'
    )
    title = models.CharField(
        max_length=255, 
        blank=True,
        verbose_name='Название:'
    )

    description = models.CharField(
        max_length=255, 
        blank=True,
        verbose_name='Описание:'
    )

    price = models.PositiveIntegerField(
        verbose_name='Цена:',
        default = 0
        )

    STATUS_CHOISES = (
        ('В ожидании', 'В ожиданни'),
        ('Принят', 'Принят'),
    )
    status = models.CharField(choices=STATUS_CHOISES, max_length=255, verbose_name='Статус заказа:')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказ'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.title}  {self.status}"
