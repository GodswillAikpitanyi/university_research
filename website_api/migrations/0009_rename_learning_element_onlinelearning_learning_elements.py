# Generated by Django 4.2.6 on 2024-01-03 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_api', '0008_rename_onlinelearningelement_learningelement_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onlinelearning',
            old_name='learning_element',
            new_name='learning_elements',
        ),
    ]