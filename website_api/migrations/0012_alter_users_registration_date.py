# Generated by Django 4.2.6 on 2024-01-21 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_api', '0011_alter_costfunding_school_fee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='registration_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]