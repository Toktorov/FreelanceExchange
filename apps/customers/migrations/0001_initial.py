# Generated by Django 3.2.6 on 2021-08-12 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='profiles')),
                ('bio', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.PositiveIntegerField(default=0)),
                ('gender', models.CharField(choices=[('m', 'Men'), ('f', 'Female'), ("I don't know", 'Trans')], max_length=255)),
            ],
        ),
    ]