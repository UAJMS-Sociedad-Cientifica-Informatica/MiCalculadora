# Generated by Django 2.2.4 on 2019-10-12 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calculadora', '0002_auto_20190914_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=10)),
                ('ru', models.IntegerField(unique=True)),
            ],
        ),
    ]