# Generated by Django 4.2.4 on 2023-09-21 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_popularcategories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popularcategories',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
