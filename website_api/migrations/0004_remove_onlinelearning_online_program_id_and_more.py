# Generated by Django 4.2.6 on 2023-12-29 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_api', '0003_remove_assessmenttype_course_details_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onlinelearning',
            name='online_program_id',
        ),
        migrations.AddField(
            model_name='onlineprogram',
            name='online_learning',
            field=models.ManyToManyField(related_name='online_program', to='website_api.onlinelearning'),
        ),
    ]