# Generated by Django 3.2.15 on 2022-10-10 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount', '0002_childcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincategory',
            name='categoryImage',
            field=models.ImageField(upload_to='', verbose_name='ecomm images'),
        ),
    ]
