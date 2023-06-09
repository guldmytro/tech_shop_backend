from rest_framework.routers import SimpleRouter
from .views import ProductViewSet

router = SimpleRouter()
router.register('products', ProductViewSet, basename='products')

urlpatterns = router.urls
