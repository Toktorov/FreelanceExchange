from django.db import models

# Create your models here.
class Profile(models.Model):
    GENDER_CHOICES = (
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина'),
        ("Оно", 'Оно'),
    )
    CUSTOMER_OR_FREELANCER_CHOISES = (
        ('Заказчик', 'Заказчик'),
        ('Фрилансер', 'Фрилансер'),
    )
    username = models.CharField(max_length=255, unique=True, verbose_name='Никнейм:')
    customer_or_freelancer = models.CharField(choices=CUSTOMER_OR_FREELANCER_CHOISES, max_length=255, verbose_name='Выбор професии:')
    bio = models.CharField(max_length=255, blank=True, null=True, verbose_name='Описание:')
    age = models.PositiveIntegerField(default=0, verbose_name='Возраст:')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=255, verbose_name='Пол:')
    balance = models.PositiveIntegerField(default = 0, verbose_name='Баланс:')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.username}  {self.customer_or_freelancer}"