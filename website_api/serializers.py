from rest_framework import serializers

from .models import (CourseDetails, Organization, Universities, AllPrograms, ELearning, Service, CostFunding,
                     Requirement)


class UniversitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universities
        fields = ('uni_id', 'user_id', 'university_name', 'university_image', 'university_address',
                  'university_website', 'facebook_handle', 'histagram_handle', 'whatsapp_handle',
                  'linkedin_handle')


class ELearningSerializer(serializers.ModelSerializer):
    learning_module = serializers.SlugRelatedField(many=True, read_only=True, slug_field='learning_module')

    class Meta:
        model = ELearning
        fields = ('program_id', 'e_learning_description', 'e_learning_participation', 'ects_availability',
                  'sign_up_availability', 'learning_module')


class ServiceSerializer(serializers.ModelSerializer):
    support = serializers.SlugRelatedField(read_only=True, slug_field='support')

    class Meta:
        model = Service
        fields = ('program_id', 'part_time_employment', 'accommodation', 'general_intl_student_support', 'support')


class CostFundingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostFunding
        fields = ('program_id', 'tuition_fee', 'semester_contribution', 'cost_of_living',
                  'funding_opportunities', 'funding_description')


class RequirementSerializer(serializers.ModelSerializer):
    academic_requirement = serializers.SlugRelatedField(many=True, read_only=True, slug_field='academic_requirement')
    language_requirement = serializers.SlugRelatedField(many=True, read_only=True, slug_field='language_requirement')
    application_deadline = serializers.SlugRelatedField(many=True, read_only=True, slug_field='application_deadline')

    class Meta:
        model = Requirement
        fields = ('program_id', 'academic_requirement', 'language_requirement', 'application_deadline')


class AllProgramsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AllPrograms
        fields = ('program_id', 'uni_id', 'program_type', 'degree_type', 'field_of_study', 'course_name', 'start_date',
                  'duration', 'tuition', 'language', 'mode_of_study', 'institution_type')



class OrganizationSerializer(serializers.ModelSerializer):
    summer_topics = serializers.SlugRelatedField(many=True, read_only=True, slug_field='summer_topics')
    summer_optional = serializers.SlugRelatedField(many=True, read_only=True, slug_field='summer_op_topics')
    winter_topics = serializers.SlugRelatedField(many=True, read_only=True, slug_field='winter_topics')
    winter_optional = serializers.SlugRelatedField(many=True, read_only=True, slug_field='winter_op_topics')
    third_semester = serializers.SlugRelatedField(many=True, read_only=True, slug_field='third_s_topics')

    class Meta:
        model = Organization
        fields = ('course_details', 'top_details', 'summer_topics', 'summer_optional', 'winter_topics',
                  'winter_optional', 'third_semester')


class CourseDetailsSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()
    assessment_type = serializers.SlugRelatedField(many=True, read_only=True, slug_field='ass_type')
    supplementary = serializers.SlugRelatedField(many=True, read_only=True, slug_field='supplementary')
    international_element = serializers.SlugRelatedField(many=True, read_only=True, slug_field='int_element')

    class Meta:
        model = CourseDetails
        fields = ('program', 'organization', 'assessment_type', 'supplementary', 'international_element',
                  'internship', 'english_language', 'german_language', 'summer', 'winter')

