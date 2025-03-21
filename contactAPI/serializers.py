from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

        extra_kwargs = {
            'email': {'required': False},
            'name': {
                'min_length': 3,
                'error_messages': {
                    'min_length': 'Name must be at least 3 characters.',
                }
            },
            'address': {'required': False},
        }