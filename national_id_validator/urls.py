from rest_framework import routers

from .views import NationalIdViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register("", NationalIdViewSet, basename="validate_national_id")

urlpatterns = router.urls
