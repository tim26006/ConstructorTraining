# Generated by Django 4.0 on 2024-03-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0006_alter_training_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top', models.CharField(max_length=50)),
                ('left', models.CharField(max_length=50)),
                ('width', models.CharField(max_length=50)),
                ('height', models.CharField(max_length=50)),
            ],
        ),
    ]