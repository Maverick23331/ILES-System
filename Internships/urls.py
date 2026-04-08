from rest_framework.routers import DefaultRouter
from .views import InternshipViewSet

router = DefaultRouter()
router.register(r'internships', InternshipViewSet, basename='internship')

urlpatterns = router.urls