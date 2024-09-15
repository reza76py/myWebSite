from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mainApp.views import BlogPostViewSet, ProjectViewSet, ContactMessageViewSet, MathCalculationViewSet

router = DefaultRouter()
router.register(r'blogposts', BlogPostViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'contactmessages', ContactMessageViewSet)
router.register(r'mathcalculations', MathCalculationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
