from products.api.viewsets import productViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', productViewset)