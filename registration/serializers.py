from rest_framework.serializers import ModelSerializer
from .models import Medical_staff
from .models import Department


class DoctorSerializer(ModelSerializer):
    class Meta:
        model=Medical_staff
        fields='__all__'

class SpecSerializer(ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'
