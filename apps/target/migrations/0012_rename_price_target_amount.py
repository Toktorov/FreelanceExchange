# Generated by Django 3.2.6 on 2021-08-15 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0011_rename_task_target'),
    ]

    operations = [
        migrations.RenameField(
            model_name='target',
            old_name='price',
            new_name='amount',
        ),
    ]
