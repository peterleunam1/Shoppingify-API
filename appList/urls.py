from rest_framework import routers 
from .views import CategoryViewSet, ProductViewSet, ProductListViewSet

router = routers.DefaultRouter()
router.register('api/category', CategoryViewSet, 'category')
router.register('api/products', ProductViewSet, 'product')
router.register('api/productlist', ProductListViewSet, 'productlist')

urlpatterns = router.urls