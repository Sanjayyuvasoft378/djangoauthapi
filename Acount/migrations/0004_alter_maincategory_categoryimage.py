# Generated by Django 3.2.15 on 2022-10-10 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount', '0003_alter_maincategory_categoryimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincategory',
            name='categoryImage',
            field=models.ImageField(upload_to='Ecomm_Images'),
        ),
    ]