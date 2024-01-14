from rest_framework import serializers

from .models import (Users, Universities, Programs, Overview, CourseDetails, AssessmentType, InternationalElement,
                     CostFunding, Requirement, Service, OnlineLearning, LearningElement)


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
        fields = ['ass_type_id', 'assessment_type']


class InternationalElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternationalElement
        fields = ['intl_element_id', 'international_element']


class CourseDetailsSerializer(serializers.ModelSerializer):
    assessment_type = AssessmentTypeSerializer(many=True)
    international_element = InternationalElementSerializer(many=True)

    class Meta:
        model = CourseDetails
        fields = ['course_details_id', 'program_id', 'course_organization', 'integrated_language',
                  'course_specialization', 'diploma_supplement', 'integrated_internship', 'integrated_foreign_language',
                  'assessment_type', 'international_element']

    def create(self, validated_data):
        assessment_type_datas = validated_data.pop('assessment_type', [])
        international_element_datas = validated_data.pop('international_element', [])

        course_details = CourseDetails.objects.create(**validated_data)

        for assessment_type_data in assessment_type_datas:
            course_details.assessment_type.create(**assessment_type_data)

        for international_element_data in international_element_datas:
            course_details.international_element.create(**international_element_data)

        return course_details

    def update(self, instance, validated_data):
        assessment_type_datas = validated_data.pop('assessment_type')
        instance.program_id = validated_data.get('program_id', instance.program_id)
        instance.course_organization = validated_data.get('course_organization', instance.course_organization)
        instance.integrated_language = validated_data.get('integrated_language', instance.integrated_language)
        instance.course_specialization = validated_data.get('course_specialization', instance.course_specialization)
        instance.diploma_supplement = validated_data.get('diploma_supplement', instance.diploma_supplement)
        instance.integrated_internship = validated_data.get('integrated_internship', instance.integrated_internship)
        instance.integrated_foreign_language = validated_data.get('integrated_foreign_language',
                                                                  instance.integrated_foreign_language)
        instance.save()
        keep_assessment_type = []
        existing_assessment_id = [A.id for A in instance.assessment_type_data]
        for assessment_type_data in assessment_type_datas:
            if "ass_type_id" in assessment_type_data.key():
                if AssessmentType.objects.filter(id=assessment_type_data["ass_type_id"]).exist():
                    A = AssessmentType.objects.get(id=assessment_type_data["ass_type_id"])
                    A.text = 


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


class LearningElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningElement
        fields = ['online_learning_id', 'learning_elements']


class OnlineLearningSerializer(serializers.ModelSerializer):
    learning_elements = LearningElementSerializer(many=True)

    class Meta:
        model = OnlineLearning
        fields = ['online_program_id', 'program_id', 'online_adaptability', 'pace_of_course',
                  'attendance_phase_in_Nigeria', 'type_of_online_learning', 'learning_elements']

    def create(self, validated_data):
        learning_elements_datas = validated_data.pop('learning_elements')
        online_learning = OnlineLearning.objects.create(**validated_data)
        for learning_elements_data in learning_elements_datas:
            online_learning.learning_elements.create(**learning_elements_data)
        return online_learning

    def update(self, instance, validated_data):
        learning_elements_datas = validated_data.pop('learning_elements')
        instance.online_program_id = validated_data.get("online_program_id", instance.online_program_id)
        instance.program_id = validated_data.get("program_id", instance.program_id)
        instance.online_adaptability = validated_data.get("online_adaptability", instance.online_adaptability)
        instance.pace_of_course = validated_data.get("pace_of_course", instance.pace_of_course)
        instance.attendance_phase_in_Nigeria = validated_data.get("attendance_phase_in_Nigeria",
                                                                  instance.attendance_phase_in_Nigeria)
        instance.type_of_online_learning = validated_data.get("type_of_online_learning",
                                                              instance.type_of_online_learning)
        instance.learning_elements.clear()
        for learning_elements_data in learning_elements_datas:
            learning_elements, created = LearningElement.objects.get_or_create(**learning_elements_data)
            instance.learning_elements.add(learning_elements)
            instance.save()
        return instance
