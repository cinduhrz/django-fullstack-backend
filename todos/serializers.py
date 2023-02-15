from .models import Todo
from rest_framework import serializers ## class to inherit from

# will make output look nice n pretty, like how we expect it
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    # contains meta info abt the serializer
    class Meta:
        # the model it will serialize
        model = Todo
        # the fields that should be included in the output
        fields = ['id', 'subject', 'details']