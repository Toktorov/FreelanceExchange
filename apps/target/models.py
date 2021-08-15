from django.db import models
from apps.users.models import Customer


# Create your models here.
class Target(models.Model):
    user = models.ForeignKey(
        Customer, 
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

    amount = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=3
    )

    status = models.BooleanField(default=False, db_index=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказ'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.title}  {self.status}"
