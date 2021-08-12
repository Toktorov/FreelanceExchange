from django.db import models

# Create your models here.
# Заказчик
class Customer(models.Model):
    GENDER_CHOICES = (
        ('m', 'Men'),
        ('f', 'Female'),
        ("I don't know", 'Trans'),
    )
    username = models.CharField(max_length=255, unique=True)
    profile = models.ImageField(upload_to='profiles', blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)
    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=255)
    balance = models.PositiveIntegerField(default = 0)

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчик'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.username} -- {self.gender}"
