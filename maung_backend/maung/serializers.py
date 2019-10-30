from rest_framework import serializers
from maung.models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['full_name', 'first_name', 'birth_date_place', 'absence_code', 'major', 'high_school', 'line_id', 'instagram', 'email', 'interest', 'hope', 'description', 'image_url']