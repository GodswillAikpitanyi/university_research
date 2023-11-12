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


class Universities(models.Model):
    # This table that registered all university programs details.
    university_name = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return f"{self.university_name}"


class AllPrograms(models.Model):
    # This table that registered all university programs details.
    universities = models.ForeignKey(Universities, on_delete=models.CASCADE)  # Foreign key referencing University table
    program_type = models.CharField(max_length=200)
    degree_type = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    start_date = models.DateField()
    semester_duration = models.CharField(max_length=200, choices=SEMESTER_CHOICES, default='1')
    tuition = models.CharField(max_length=200)
    language = models.CharField(max_length=50, choices=LANGUAGES_CHOICE, default='ENGLISH')
    mode_of_study = models.CharField(max_length=200)
    institution_type = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.universities} {self.program_type} {self.course_name}"

    class Meta:
        ordering = ['universities']


class CourseDetails(models.Model):
    # This is the table that show details information of individual course
    internship = models.CharField(max_length=5000, null=True)  # Hashed and salted
    summer = models.CharField(max_length=5000, null=True)
    winter = models.CharField(max_length=5000, null=True)
    english_language = models.CharField(max_length=10, choices=LANGUAGE_AVAILABILITY, default='YES')
    german_language = models.CharField(max_length=10, choices=LANGUAGE_AVAILABILITY, default='YES')
    program = models.ForeignKey(AllPrograms, related_name="program", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.program}"

    class Meta:
        ordering = ['program']


class Organization(models.Model):
    # This is the table that show details information of individual course
    course_details = models.ForeignKey(CourseDetails, related_name='organizations', null=True,
                                       on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course_details}"


class AssessmentType(models.Model):
    # This tables contains details information about winter program
    ass_type = models.CharField(max_length=2000)
    course_details = models.ForeignKey(CourseDetails, related_name='assessment_type', null=True,
                                       on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ass_type}"


class Supplementary(models.Model):
    # This tables contains details information about winter program
    supplementary = models.CharField(max_length=2000)
    course_details = models.ForeignKey(CourseDetails, related_name='supplementary', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.supplementary}"


class InternationalElement(models.Model):
    # This tables contains details information about winter program
    int_element = models.CharField(max_length=2000)
    course_details = models.ForeignKey(CourseDetails, related_name='international_element', null=True,
                                       on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.int_element}"


class TopDetails(models.Model):
    # This tables contains details information about winter program
    details = models.CharField(max_length=5000)
    organization = models.ForeignKey(Organization, related_name='top_details', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.details}"


class Summer(models.Model):
    # This tables contains details information about winter program
    summer_topics = models.CharField(max_length=5000)
    organization = models.ForeignKey(Organization, related_name='summer_topics', null=True,
                                     on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.summer_topics}"


class SummerOptional(models.Model):
    # This tables contains details information about summer program
    summer_op_topics = models.CharField(max_length=5000)
    organization = models.ForeignKey(Organization, related_name='summer_optional', null=True,
                                     on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.summer_op_topics}"


class Winter(models.Model):
    # This tables contains details information about winter program
    winter_id = models.AutoField(primary_key=True)  # primary key
    winter_topics = models.CharField(max_length=5000)
    organization = models.ForeignKey(Organization, related_name='winter_topics', null=True,
                                     on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.winter_id} {self.winter_topics}"


class WinterOptional(models.Model):
    # This tables contains details information about winter program
    winter_op_topics = models.CharField(max_length=5000)
    organization = models.ForeignKey(Organization, related_name='winter_optional', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.winter_op_topics}"


class ThirdSemester(models.Model):
    # This tables contains details information about winter program
    third_s_topics = models.CharField(max_length=200)
    organization = models.ForeignKey(Organization, related_name='third_semester', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.third_s_topics}"
