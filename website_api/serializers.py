from rest_framework import serializers

from .models import (Users, Universities, Programs, Overview, CourseDetails, AssessmentType, InternationalElement,
                     CostFunding, Requirement, Service, OnlineLearning, OnlineLearningElement)


class UniversitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Universities
        fields = ['uni_id', 'user_id', 'institution_name', 'institution_address', 'institution_location',
                  'about_university', 'state', 'institution_logo', 'institution_image']


class ProgramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programs
        fields = ('program_id', 'uni_id', 'coordinator_name', 'coordinator_address', 'coordinator_phone',
                  'coordinator_phone', 'coordinator_email', 'program_title', 'program_abbreviation',
                  'degree_abbreviation', 'program_website', 'instagram_url', 'linkedin_url', 'facebook_url',
                  'twitter_url', 'youtube_url')



class OverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Overview
        fields = ['overview_id', 'program_id', 'degree', 'field_of_study', 'mode_of_study', 'languages', 'start_date',
                  'tuition_fee', 'school_fee', 'thematic_area', 'program_type', 'teaching_language', 'program_duration',
                  'application_deadline', 'combine_master_phd', 'joint_degree_program']


class AssessmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentType
        fields = ['ass_type_id', 'course_details_id', 'assessment_type']



class InternationalElementSerializer(serializers.ModelSerializer):

    class Meta:
        model = InternationalElement
        fields = ['intl_element_id', 'course_details_id', 'international_element']


class CourseDetailsSerializer(serializers.ModelSerializer):
    assessment_type = AssessmentTypeSerializer(many=True)
    international_element = InternationalElementSerializer(many=True)

    class Meta:
        model = CourseDetails
        fields = ['course_details_id', 'program_id', 'course_organization', 'integrated_language',
                  'course_specialization', 'diploma_supplement', 'integrated_internship', 'integrated_foreign_language',
                  'assessment_type', 'international_element']

class CostFundingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostFunding
        fields = ['cost_f_id', 'program_id', 'tuition_fee', 'cost_of_living', 'funding_opportunities',
                  'funding_description']


class RequirementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requirement
        fields = ['req_id', 'program_id', 'academic_requirement', 'language_requirement', 'application_requirement',
                  'submit_application_to']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['service_id', 'program_id', 'accommodation', 'general_intl_student_support', 'part_time_employment',
                  'career_advisory_service', 'special_or_non_special_support']


class OnlineLearningElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineLearningElement
        fields = ['online_learning_id', 'online_program_id', 'online_learning_element']


class OnlineLearningSerializer(serializers.ModelSerializer):
    online_learning_element = OnlineLearningElementSerializer(many=True)

    class Meta:
        model = OnlineLearning
        fields = ['online_program_id', 'program_id', 'online_adaptability', 'pace_of_course',
                  'attendance_phase_in_Nigeria', 'type_of_online_learning', 'online_learning_element']

    def create(self, validated_data):
        online_learning_element_data = validated_data.pop('program_details')
        online_learning_element = OnlineLearning.objects.create(**online_learning_element_data)
        online_learning = OnlineLearning.objects.create(online_learning_element=online_learning_element)
        return online_learning





