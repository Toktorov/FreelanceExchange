# Generated by Django 3.2.6 on 2021-08-15 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0007_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='price',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=12),
        ),
    ]
