# Generated by Django 4.2.6 on 2024-01-03 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_api', '0007_onlinelearningelement_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OnlineLearningElement',
            new_name='LearningElement',
        ),
        migrations.RenameField(
            model_name='learningelement',
            old_name='online_learning_element',
            new_name='learning_element',
        ),
        migrations.RenameField(
            model_name='onlinelearning',
            old_name='online_learning',
            new_name='learning_element',
        ),
    ]
