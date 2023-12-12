from django.db import models

SEMESTER_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
)

LANGUAGES_CHOICE = (
    ("ENGLISH", "ENGLISH"),
    ("GERMAN", "GERMAN"),
)

LANGUAGE_AVAILABILITY = (
    ("YES", "YES"),
    ("NO", "NO"),
)

GENDER = (
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE")
)


class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=500)
    username = models.CharField(max_length=100, unique=True)
    user_type = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER, default='MALE')
    registration_date = models.DateField()

    def __str__(self):
        return f"{self.user_id} {self.username}"


class Universities(models.Model):
    # This table that registered all university programs details.
    uni_id = models.BigAutoField(primary_key=True)
    user_id = models.OneToOneField(Users, related_name="universities", on_delete=models.CASCADE, null=True)
    university_name = models.CharField(max_length=500, unique=True)
    university_address = models.CharField(max_length=2000)
    university_website = models.CharField(max_length=500)
    facebook_handle = models.CharField(max_length=1000)
    histagram_handle = models.CharField(max_length=1000)
    whatsapp_handle = models.CharField(max_length=1000)
    linkedin_handle = models.CharField(max_length=1000)

    def upload_photo(self, filename):
        path = 'images/university_photo/{}' + filename
        return path

    university_image = models.ImageField(upload_to=upload_photo)

    def __str__(self):
        return f"{self.university_name}"


class AllPrograms(models.Model):
    # This table that registered all university programs details.
    program_id = models.BigAutoField(primary_key=True)
    uni_id = models.ForeignKey(Universities, related_name="all_programs", on_delete=models.CASCADE)  # Foreign key referencing University table
    program_type = models.CharField(max_length=200)
    degree_type = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    start_date = models.DateField()
    duration = models.CharField(max_length=200, choices=SEMESTER_CHOICES, default='1')
    tuition = models.CharField(max_length=200)
    language = models.CharField(max_length=50, choices=LANGUAGES_CHOICE, default='ENGLISH')
    mode_of_study = models.CharField(max_length=200)
    institution_type = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.uni_id} {self.program_type} {self.course_name}"

    class Meta:
        ordering = ['uni_id']


class Service(models.Model):
    service_id = models.BigAutoField(primary_key=True)
    program_id = models.OneToOneField(AllPrograms, related_name="service", on_delete=models.CASCADE)
    part_time_employment = models.CharField(max_length=3000)
    accommodation = models.CharField(max_length=3000)
    general_intl_student_support = models.CharField(max_length=3000)

    def __str__(self):
        return f"{self.service_id} {self.accommodation}"


class Support(models.Model):
    support_id = models.BigAutoField(primary_key=True)
    service_id = models.OneToOneField(Service, related_name="support", on_delete=models.CASCADE)
    support = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.support_id} {self.support}"


class Requirement(models.Model):
    req_id = models.BigAutoField(primary_key=True)
    program_id = models.OneToOneField(AllPrograms, related_name="requirement", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.req_id}"


class AcademicRequirement(models.Model):
    acad_req_id = models.BigAutoField(primary_key=True)
    req_id = models.ForeignKey(Requirement, related_name="academic_requirement", on_delete=models.CASCADE)
    admission_requirement = models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.acad_req_id} {self.admission_requirement}"


class LanguageRequirement(models.Model):
    lang_req_id = models.BigAutoField(primary_key=True)
    req_id = models.ForeignKey(Requirement, related_name="language_requirement", on_delete=models.CASCADE)
    language_requirement = models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.lang_req_id} {self.language_requirement}"


class ApplicationDeadline(models.Model):
    app_d_id = models.BigAutoField(primary_key=True)
    req_id = models.ForeignKey(Requirement, related_name="application_deadline", on_delete=models.CASCADE)
    application_deadline = models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.app_d_id} {self.application_deadline}"


class ELearning(models.Model):
    e_learn_id = models.BigAutoField(primary_key=True)
    program_id = models.OneToOneField(AllPrograms, related_name="e_learning", on_delete=models.CASCADE)
    online_course = models.CharField(max_length=10)
    e_learning_description = models.CharField(max_length=2000)
    e_learning_participation = models.CharField(max_length=10)
    ects_availability = models.CharField(max_length=10)
    sign_up_availability = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.e_learn_id} {self.e_learning_description}"


class LearningModule(models.Model):
    learn_mod_id = models.BigAutoField(primary_key=True)
    e_learn_id = models.ForeignKey(ELearning, related_name='learning_module', on_delete=models.CASCADE)
    learning_module = models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.learn_mod_id} {self.learning_module}"


class CostFunding(models.Model):
    cost_f_id = models.BigAutoField(primary_key=True)
    program_id = models.OneToOneField(AllPrograms, related_name="cost_funding", on_delete=models.CASCADE)
    tuition_fee = models.CharField(max_length=1000)
    semester_contribution = models.DecimalField(max_digits=6, decimal_places=2)
    cost_of_living = models.CharField(max_length=2000)
    funding_opportunities = models.CharField(max_length=2000)
    funding_description = models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.cost_f_id} {self.cost_of_living}"


class CourseDetails(models.Model):
    # This is the table that show details information of individual course
    course_details_id = models.BigAutoField(primary_key=True)
    internship = models.CharField(max_length=5000, null=True)  # Hashed and salted
    summer = models.CharField(max_length=5000, null=True)
    winter = models.CharField(max_length=5000, null=True)
    english_language = models.CharField(max_length=10, choices=LANGUAGE_AVAILABILITY, default='YES')
    german_language = models.CharField(max_length=10, choices=LANGUAGE_AVAILABILITY, default='YES')
    program = models.OneToOneField(AllPrograms, related_name="course_details", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course_details_id} {self.program} "

    class Meta:
        ordering = ['course_details_id']


class AssessmentType(models.Model):
    # This tables contains details information about winter program
    ass_id = models.BigAutoField(primary_key=True)
    ass_type = models.CharField(max_length=2000)
    course_details = models.ForeignKey(CourseDetails, related_name='assessment_type', null=True,
                                       on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ass_id} {self.ass_type}"


class Supplementary(models.Model):
    # This tables contains details information about winter program
    sup_id = models.BigAutoField(primary_key=True)
    supplementary = models.CharField(max_length=2000)
    course_details = models.ForeignKey(CourseDetails, related_name='supplementary', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sup_id} {self.supplementary}"


class InternationalElement(models.Model):
    # This tables contains details information about winter program
    int_id = models.BigAutoField(primary_key=True)
    int_element = models.CharField(max_length=2000)
    course_details = models.ForeignKey(CourseDetails, related_name='international_element', null=True,
                                       on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.int_id} {self.int_element}"


class Organization(models.Model):
    # This is the table that show details information of individual course
    org_id = models.BigAutoField(primary_key=True)
    top_details = models.CharField(max_length=2000)
    course_details = models.OneToOneField(CourseDetails, related_name='organization', null=True,
                                          on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.org_id} {self.course_details}"



class SummerTopics(models.Model):
    # This tables contains details information about winter program
    sum_id = models.BigAutoField(primary_key=True)
    summer_topics = models.CharField(max_length=5000)
    organization = models.ForeignKey(Organization, related_name='summer_topics', null=True,
                                     on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.sum_id} {self.summer_topics}"


class SummerOptionalTopics(models.Model):
    # This tables contains details information about summer program
    sum_opt_id = models.BigAutoField(primary_key=True)
    summer_op_topics = models.CharField(max_length=5000)
    organization = models.ForeignKey(Organization, related_name='summer_optional', null=True,
                                     on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sum_opt_id} {self.summer_op_topics}"


class WinterTopics(models.Model):
    # This tables contains details information about winter program
    winter_id = models.AutoField(primary_key=True)  # primary key
    winter_topics = models.CharField(max_length=5000)
    organization = models.ForeignKey(Organization, related_name='winter_topics', null=True,
                                     on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.winter_id} {self.winter_topics}"


class WinterOptionalTopics(models.Model):
    # This tables contains details information about winter program
    wint_opt_id = models.BigAutoField(primary_key=True)
    winter_op_topics = models.CharField(max_length=5000)
    organization = models.ForeignKey(Organization, related_name='winter_optional', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.wint_opt_id} {self.winter_op_topics}"


class ThirdSemester(models.Model):
    # This tables contains details information about winter program
    third_sem_id = models.BigAutoField(primary_key=True)
    third_s_topics = models.CharField(max_length=200)
    organization = models.ForeignKey(Organization, related_name='third_semester', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.third_sem_id} {self.third_s_topics}"
