from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import TitleViewSet, ResultViewSet, SearchViewSet, LettersViewSet, AbsoluteViewSet

router = DefaultRouter()
router.register(r'titles', TitleViewSet)
router.register(r'results', ResultViewSet)
router.register(r'search', SearchViewSet)
router.register(r'letters', LettersViewSet)
router.register(r'absolute', AbsoluteViewSet)

urlpatterns = router.urls
