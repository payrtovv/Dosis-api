from rest_framework import serializers

from .models import *

# serializers.py
class MedicineSerializer(serializers.ModelSerializer):
    presentation_display = serializers.CharField(
        source='get_presentation_display', read_only=True
    )

    class Meta:
        model = Medicine
        fields = [
            'id', 'name', 'generic_name' ,'brand_or_laboratory',
            'concentration', 'presentation', 'presentation_display',
            'description', 'contraindications',
            'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']