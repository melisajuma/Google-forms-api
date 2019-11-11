from rest_framework import serializers
from .models import someModel

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= someModel
        fields = ('name', 'agegroup','fieldofStudy','cryptoknowledge','whatwoulddiscourageyou')