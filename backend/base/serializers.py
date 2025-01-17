from rest_framework import serializers

from .models import ClubMember


class ClubMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubMember
        fields = ("name", "phone", "attendence", "is_admin")
