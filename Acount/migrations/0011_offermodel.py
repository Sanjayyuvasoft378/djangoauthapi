# Generated by Django 3.2.15 on 2022-10-20 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount', '0010_discountmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offerName', models.CharField(max_length=255)),
                ('offerType', models.CharField(max_length=255)),
                ('offerValue', models.IntegerField()),
            ],
            options={
                'db_table': 'Offer',
            },
        ),
    ]