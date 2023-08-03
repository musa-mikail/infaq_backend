from rest_framework import serializers
from .models import Mosque

class MosqueListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mosque
        fields = [
            'id',
            'mosque_name',
            'mosque_focal_point',
            'mosque_address',
            'mosque_phone',
            'mosque_bank',
            'mosque_account',
            'mosque_status'
        ]
class MosqueDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mosque
        fields = [
                'mosque_name',
                'mosque_focal_point',
                'mosque_address',
                'mosque_email',
                'mosque_phone',
                'mosque_website',
                'mosque_city',
                'mosque_state',
                'mosque_bank',
                'mosque_account',
                'mosque_status',
                'mosque_date_created',
                'mosque_date_disabled',
                'mosque_image'          ]
