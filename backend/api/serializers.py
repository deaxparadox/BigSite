from rest_framework import serializers 

from extras.models import india

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = india.State
        fields = "__all__"