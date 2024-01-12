# Generated by Django 4.2.6 on 2023-12-29 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_api', '0002_rename_course_details_id_onlinelearning_online_program_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assessmenttype',
            name='course_details_id',
        ),
        migrations.RemoveField(
            model_name='internationalelement',
            name='course_details_id',
        ),
        migrations.RemoveField(
            model_name='onlinelearning',
            name='online_program_id',
        ),
        migrations.AddField(
            model_name='assessmenttype',
            name='course_details_id',
            field=models.ManyToManyField(related_name='assessment_type', to='website_api.coursedetails'),
        ),
        migrations.AddField(
            model_name='internationalelement',
            name='course_details_id',
            field=models.ManyToManyField(related_name='international_element', to='website_api.coursedetails'),
        ),
        migrations.AddField(
            model_name='onlinelearning',
            name='online_program_id',
            field=models.ManyToManyField(related_name='online_learning', to='website_api.onlineprogram'),
        ),
    ]