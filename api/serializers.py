from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from main.models import Customer, Course

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'phone_number', 'email', 'course', 'checked')

class CourseSerailizers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name')