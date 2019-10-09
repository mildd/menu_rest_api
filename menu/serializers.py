from rest_framework import fields, serializers

from .models import *


class OrderModelSerializer(serializers.HyperlinkedModelSerializer):
    thai_choice = fields.MultipleChoiceField(choices=THAI_MENU)
    russian_choice = fields.MultipleChoiceField(choices=RUSSIAN_MENU)
    french_choice = fields.MultipleChoiceField(choices=FRENCH_MENU)

    class Meta:
        model = OrderModel
        fields = ('id', 'thai_choice', 'russian_choice', 'french_choice')

