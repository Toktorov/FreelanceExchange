# Generated by Django 3.2.6 on 2021-08-15 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=12),
        ),
    ]
