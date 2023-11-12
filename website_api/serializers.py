from rest_framework import serializers
from .models import (CourseDetails, Organization, Universities, AllPrograms, AssessmentType, Supplementary,
                     InternationalElement, Summer, SummerOptional, Winter, WinterOptional)


class UniversitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universities
        fields = ('id', 'university_name')




class AllProgramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllPrograms
        fields = ('id', 'universities', 'program_type', 'degree_type', 'field_of_study', 'course_name', 'start_date',
                  'semester_duration', 'tuition', 'language', 'mode_of_study', 'institution_type')


class OrganizationSerializer(serializers.ModelSerializer):
    top_details = serializers.SlugRelatedField(many=True, read_only=True, slug_field='details')
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
    organization = OrganizationSerializer(many=True, read_only=True)
    assessment_type = serializers.SlugRelatedField(many=True, read_only=True, slug_field='ass_type')
    supplementary = serializers.SlugRelatedField(many=True, read_only=True, slug_field='supplementary')
    international_element = serializers.SlugRelatedField(many=True, read_only=True, slug_field='int_element')

    class Meta:
        model = CourseDetails
        fields = ('program', 'organization', 'assessment_type', 'supplementary', 'international_element', 'internship',
                  'english_language', 'german_language', 'summer', 'winter')




