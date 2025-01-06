from rest_framework import serializers
def no_number(value):
    if any(char.isdigit() for char in value):
        raise serializers.ValidationError('Name should not contain number')

