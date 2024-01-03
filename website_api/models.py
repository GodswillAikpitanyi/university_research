from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



AVAILABILITY_CHOICES = (
    ("YES", "YES"),
    ("NO", "NO"),
)

GENDER = (
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE")
)

USER_ROLES = (
    ("NORMAL", "NORMAL"),
    ("POSTER", "POSTER")
)


class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    user_role = models.CharField(max_length=50, choices=USER_ROLES, default='NORMAL')
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER, default='MALE')
    registration_date = models.DateField()

    def __str__(self):
        return f"{self.user_id} {self.username}"


class Universities(models.Model):
    # This table that registered all university programs details.
    uni_id = models.BigAutoField(primary_key=True)
    user_id = models.OneToOneField(Users, related_name="universities", on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=500, unique=True)
    institution_address = models.CharField(max_length=2000)
    institution_location = models.CharField(max_length=200)
    about_university = models.CharField(max_length=5000)
    state = models.CharField(max_length=50, null=True, blank=True)

    def upload_logo(self, filename):
        path = 'images/institution_logo/{}' + filename
        return path
    institution_logo = models.ImageField(upload_to=upload_logo)

    def upload_photo(self, filename):
        path = 'images/institution_photo/{}' + filename
        return path
    institution_image = models.ImageField(upload_to=upload_photo, null=True, blank=True)

    def __str__(self):
        return f"{self.uni_id} {self.institution_name}"


class Programs(models.Model):
    # This table that registered all university programs details.
    program_id = models.BigAutoField(primary_key=True)
    uni_id = models.ForeignKey(Universities, related_name="program_details", on_delete=models.CASCADE)  # Foreign key referencing University table
    coordinator_name = models.CharField(max_length=1000)
    coordinator_address = models.CharField(max_length=2000)
    coordinator_phone = PhoneNumberField()
    coordinator_email = models.EmailField(max_length=100, unique=True)
    program_title = models.CharField(max_length=200)
    program_abbreviation = models.CharField(max_length=200, null=True, blank=True)
    degree_abbreviation = models.CharField(max_length=50)
    program_website = models.CharField(max_length=1000, null=True, blank=True)
    instagram_url = models.CharField(max_length=1000, null=True, blank=True)
    linkedin_url = models.CharField(max_length=1000, null=True, blank=True)
    facebook_url = models.CharField(max_length=1000, null=True, blank=True)
    twitter_url = models.CharField(max_length=1000, null=True, blank=True)
    youtube_url = models.CharField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return f"{self.uni_id} {self.program_title}"


class Overview(models.Model):
    # This table that registered all university programs details.
    overview_id = models.BigAutoField(primary_key=True)
    program_id = models.OneToOneField(Programs, related_name="overview", on_delete=models.CASCADE)  # Foreign key referencing University table
    degree = models.CharField(max_length=500)
    field_of_study = models.CharField(max_length=200)
    mode_of_study = models.CharField(max_length=200)
    languages = models.CharField(max_length=500, null=True, blank=True)
    start_date = models.DateField()
    tuition_fee = models.CharField(max_length=1000, choices=AVAILABILITY_CHOICES, default='YES')
    school_fee = models.CharField(max_length=1000, choices=AVAILABILITY_CHOICES, default='YES')
    thematic_area = models.CharField(max_length=1000)
    program_type = models.CharField(max_length=1000)
    teaching_language = models.CharField(max_length=1000)
    program_duration = models.CharField(max_length=1000)
    application_deadline = models.DateField()
    combine_master_phd = models.CharField(max_length=1000, null=True, blank=True, choices=AVAILABILITY_CHOICES, default='YES')
    joint_degree_program = models.CharField(max_length=1000, null=True, blank=True, choices=AVAILABILITY_CHOICES, default='YES')

    def __str__(self):
        return f"{self.program_id} {self.degree}"




class AssessmentType(models.Model):
    ass_type_id = models.BigAutoField(primary_key=True)
    assessment_type = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.ass_type_id} {self.assessment_type}"


class InternationalElement(models.Model):
    intl_element_id = models.BigAutoField(primary_key=True)
    international_element = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.intl_element_id} {self.international_element}"


class CourseDetails(models.Model):
    # This is the table that show details information of individual course
    course_details_id = models.BigAutoField(primary_key=True)
    program_id = models.OneToOneField(Programs, related_name="course_details", on_delete=models.CASCADE)
    course_organization = models.CharField(max_length=5000)
    integrated_language = models.CharField(max_length=5000, null=True, blank=True, choices=AVAILABILITY_CHOICES, default='YES')
    course_specialization = models.CharField(max_length=5000)
    diploma_supplement = models.CharField(max_length=5000, null=True, blank=True, choices=AVAILABILITY_CHOICES, default='YES')
    integrated_internship = models.CharField(max_length=5000, null=True, blank=True, choices=AVAILABILITY_CHOICES, default='YES')
    integrated_foreign_language = models.CharField(max_length=5000, null=True, blank=True)
    assessment_type = models.ManyToManyField(AssessmentType, related_name='course_details')
    international_element = models.ManyToManyField(InternationalElement, related_name='course_details')

    def __str__(self):
        return f"{self.course_details_id} {self.course_organization}"


class CostFunding(models.Model):
    cost_f_id = models.BigAutoField(primary_key=True)
    program_id = models.OneToOneField(Programs, related_name="cost_funding", on_delete=models.CASCADE)
    tuition_fee = models.DecimalField(max_digits=6, decimal_places=1)
    school_fee = models.DecimalField(max_digits=6, decimal_places=1)
    cost_of_living = models.CharField(max_length=2000)
    funding_opportunities = models.CharField(max_length=2000, null=True, blank=True)
    funding_description = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return f"{self.cost_f_id} {self.tuition_fee}"


class Requirement(models.Model):
    req_id = models.BigAutoField(primary_key=True)
    program_id = models.OneToOneField(Programs, related_name="requirement", on_delete=models.CASCADE)
    academic_requirement = models.CharField(max_length=3000)
    language_requirement = models.CharField(max_length=3000, null=True, blank=True)
    application_requirement = models.CharField(max_length=3000)
    submit_application_to = models.CharField(max_length=3000, null=True, blank=True)

    def __str__(self):
        return f"{self.req_id} {self.academic_requirement}"


class Service(models.Model):
    service_id = models.BigAutoField(primary_key=True)
    program_id = models.OneToOneField(Programs, related_name="service", on_delete=models.CASCADE)
    accommodation = models.CharField(max_length=3000)
    general_intl_student_support = models.CharField(max_length=3000)
    part_time_employment = models.CharField(max_length=3000, null=True, blank=True)
    career_advisory_service = models.CharField(max_length=3000, null=True, blank=True)
    special_or_non_special_support = models.CharField(max_length=3000, null=True, blank=True)

    def __str__(self):
        return f"{self.service_id} {self.general_intl_student_support}"


class LearningElement(models.Model):
    online_learning_id = models.BigAutoField(primary_key=True)
    learning_element = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.online_learning_id} {self.learning_element}"


class OnlineLearning(models.Model):
    online_program_id = models.BigAutoField(primary_key=True)
    program_id = models.OneToOneField(Programs, related_name="online_learning", on_delete=models.CASCADE,
                                      null=True, blank=True)
    online_adaptability = models.CharField(max_length=100, null=True, blank=True)
    pace_of_course = models.CharField(max_length=100, null=True, blank=True)
    attendance_phase_in_Nigeria = models.CharField(max_length=100, null=True, blank=True)
    type_of_online_learning = models.CharField(max_length=100, null=True, blank=True)
    learning_element = models.ManyToManyField(LearningElement, related_name="online_learning")

    def __str__(self):
        return f"{self.online_program_id} {self.online_adaptability}"






