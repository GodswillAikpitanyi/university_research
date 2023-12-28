# Generated by Django 4.2.6 on 2023-12-28 09:18

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import website_api.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllPrograms',
            fields=[
                ('program_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('coordinator_name', models.CharField(max_length=1000)),
                ('coordinator_address', models.CharField(max_length=2000)),
                ('coordinator_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('coordinator_email', models.EmailField(max_length=100, unique=True)),
                ('program_title', models.CharField(max_length=200)),
                ('program_abbreviation', models.CharField(max_length=200, null=True)),
                ('degree_abbreviation', models.CharField(max_length=50)),
                ('program_website', models.CharField(max_length=1000, null=True)),
                ('instagram_url', models.CharField(max_length=1000, null=True)),
                ('linkedin_url', models.CharField(max_length=1000, null=True)),
                ('facebook_url', models.CharField(max_length=1000, null=True)),
                ('twitter_url', models.CharField(max_length=1000, null=True)),
                ('youtube_url', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseDetails',
            fields=[
                ('course_details_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('course_organization', models.CharField(max_length=5000)),
                ('integrated_language', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=5000, null=True)),
                ('course_specialization', models.CharField(max_length=5000)),
                ('diploma_supplement', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=5000, null=True)),
                ('integrated_internship', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=5000, null=True)),
                ('integrated_foreign_language', models.CharField(max_length=5000, null=True)),
                ('program_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='course_details', to='website_api.allprograms')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('user_role', models.CharField(choices=[('NORMAL', 'NORMAL'), ('POSTER', 'POSTER')], default='NORMAL', max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='MALE', max_length=10)),
                ('registration_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Universities',
            fields=[
                ('uni_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('institution_name', models.CharField(max_length=500, unique=True)),
                ('institution_address', models.CharField(max_length=2000)),
                ('institution_location', models.CharField(max_length=200)),
                ('about_university', models.CharField(max_length=5000)),
                ('state', models.CharField(max_length=50, null=True)),
                ('institution_logo', models.ImageField(upload_to=website_api.models.Universities.upload_logo)),
                ('institution_image', models.ImageField(null=True, upload_to=website_api.models.Universities.upload_photo)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='universities', to='website_api.users')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('accommodation', models.CharField(max_length=3000)),
                ('general_intl_student_support', models.CharField(max_length=3000)),
                ('part_time_employment', models.CharField(max_length=3000, null=True)),
                ('career_advisory_service', models.CharField(max_length=3000, null=True)),
                ('special_or_non_special_support', models.CharField(max_length=3000, null=True)),
                ('program_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='website_api.allprograms')),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('req_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('academic_requirement', models.CharField(max_length=3000)),
                ('language_requirement', models.CharField(max_length=3000, null=True)),
                ('application_requirement', models.CharField(max_length=3000)),
                ('submit_application_to', models.CharField(max_length=3000, null=True)),
                ('program_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='requirement', to='website_api.allprograms')),
            ],
        ),
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('overview_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('degree', models.CharField(max_length=500)),
                ('field_of_study', models.CharField(max_length=200)),
                ('mode_of_study', models.CharField(max_length=200)),
                ('languages', models.CharField(max_length=500, null=True)),
                ('start_date', models.DateField()),
                ('tuition_fee', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=1000)),
                ('school_fee', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=1000)),
                ('thematic_area', models.CharField(max_length=1000)),
                ('program_type', models.CharField(max_length=1000)),
                ('teaching_language', models.CharField(max_length=1000)),
                ('program_duration', models.CharField(max_length=1000)),
                ('application_deadline', models.DateField()),
                ('combine_master_phd', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=1000, null=True)),
                ('joint_degree_program', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=1000, null=True)),
                ('program_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='overview', to='website_api.allprograms')),
            ],
        ),
        migrations.CreateModel(
            name='OnlineProgram',
            fields=[
                ('online_program_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('online_adaptability', models.CharField(max_length=10)),
                ('pace_of_course', models.CharField(max_length=10)),
                ('attendance_phase_in_Nigeria', models.CharField(max_length=10)),
                ('type_of_online_learning', models.CharField(max_length=10)),
                ('program_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='online_program', to='website_api.allprograms')),
            ],
        ),
        migrations.CreateModel(
            name='OnlineLearning',
            fields=[
                ('online_learning_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('online_learning', models.CharField(max_length=500)),
                ('course_details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='online_learning', to='website_api.coursedetails')),
            ],
        ),
        migrations.CreateModel(
            name='InternationalElement',
            fields=[
                ('intl_element_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('international_element', models.CharField(max_length=500)),
                ('course_details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='international_element', to='website_api.coursedetails')),
            ],
        ),
        migrations.CreateModel(
            name='CostFunding',
            fields=[
                ('cost_f_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tuition_fee', models.DecimalField(decimal_places=1, max_digits=6)),
                ('school_fee', models.DecimalField(decimal_places=1, max_digits=6)),
                ('cost_of_living', models.CharField(max_length=2000)),
                ('funding_opportunities', models.CharField(max_length=2000)),
                ('funding_description', models.CharField(max_length=2000)),
                ('program_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cost_funding', to='website_api.allprograms')),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentType',
            fields=[
                ('ass_type_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('assessment_type', models.CharField(max_length=500)),
                ('course_details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessment_type', to='website_api.coursedetails')),
            ],
        ),
        migrations.AddField(
            model_name='allprograms',
            name='uni_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_programs', to='website_api.universities'),
        ),
    ]
