# Generated by Django 4.2.7 on 2023-11-22 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colchon',
            name='boton',
            field=models.BooleanField(default=False),
        ),
    ]
