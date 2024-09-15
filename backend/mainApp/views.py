from rest_framework import viewsets
from .models import BlogPost, Project, ContactMessage, MathCalculation
from .serializers import BlogPostSerializer, ProjectSerializer, ContactMessageSerializer, MathCalculationSerializer
from rest_framework.decorators import action
from django.http import JsonResponse

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

class MathCalculationViewSet(viewsets.ModelViewSet):
    queryset = MathCalculation.objects.all()
    serializer_class = MathCalculationSerializer

    @action(detail=False, methods=['post'])
    def calculate(self, request):
        input_data = request.data.get('input_data', {})
        result = sum(input_data.get('numbers', []))
        calculation = MathCalculation.objects.create(
            operation="addition",
            input_data=input_data,
            result=result
        )
        return JsonResponse({'result': result})
