# Generated by Django 4.2.3 on 2023-09-03 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
