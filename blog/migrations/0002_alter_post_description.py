# Generated by Django 3.2.8 on 2022-10-16 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=2500),
        ),
    ]
