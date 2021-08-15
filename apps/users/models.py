from django.db import models
from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()


# Create your models here.
class Customer(models.Model):
    GENDER_CHOICES = (
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина'),
        ("Оно", 'Оно'),
    )
    username = models.CharField(max_length=255, unique=True, verbose_name='Никнейм:')
    bio = models.CharField(max_length=255, blank=True, null=True, verbose_name='Описание:')
    age = models.PositiveIntegerField(default=0, verbose_name='Возраст:')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=255, verbose_name='Пол:')
    amount = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=3
    )

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчик'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.username}"

class Freelancer(models.Model):
    GENDER_CHOICES = (
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина'),
        ("Оно", 'Оно'),
    )
    username = models.CharField(max_length=255, unique=True, verbose_name='Никнейм:')
    bio = models.CharField(max_length=255, blank=True, null=True, verbose_name='Описание:')
    age = models.PositiveIntegerField(default=0, verbose_name='Возраст:')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=255, verbose_name='Пол:')
    amount = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=3
    )

    class Meta:
        verbose_name = 'Фрилансер'
        verbose_name_plural = 'Фрилансер'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.username}"

class Transaction(models.Model):
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=3
    )
    date = models.DateTimeField(auto_now_add=True)

    from_account = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    to_account = models.ForeignKey(
        Freelancer,
        on_delete=models.CASCADE
    )

    commentary = models.CharField(max_length=255)

    def __str__(self):
        return f'Trancaction from {self.from_account} to {self.to_account} ({self.date})'

    @classmethod
    def deposit(cls, customer, freelancer, amount):
        with transaction.atomic():
            account = (
                cls.objects
                .select_for_update()
                .get(customer=customer)
            )
      
            customer -= amount
            freelancer += amount
            customer.save()
        return account
