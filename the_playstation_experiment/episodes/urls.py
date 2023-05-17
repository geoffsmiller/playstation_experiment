from rest_framework import routers
from episodes.views import EpisodeViewSet, SeriesViewSet

router = routers.SimpleRouter()
router.register(r"episodes", EpisodeViewSet)
router.register(r"series", SeriesViewSet)
urlpatterns = router.urls
