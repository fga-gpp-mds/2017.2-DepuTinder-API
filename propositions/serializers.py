from rest_framework import serializers
from .models import Propositions

class PropositionsSerializer(serializers.Serializer):
    class Meta:
        model = Propositions
        fields = ('propositionID', 'propositionTitle', 'propositionSubTitle', 'propositionDescription', 'propositionAuthor')