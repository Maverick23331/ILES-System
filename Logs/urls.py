from rest_framework.routers import DefaultRouter
from .views import WorkLogViewSet

router = DefaultRouter()
router.register(r'worklogs', WorkLogViewSet, basename='worklog')

urlpatterns = router.urls