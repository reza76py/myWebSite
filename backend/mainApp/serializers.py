from rest_framework import serializers
from .models import BlogPost, Project, ContactMessage, MathCalculation

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'

class MathCalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MathCalculation
        fields = '__all__'
