from quickcommerce.api.viewsets import productViewset, customerViewset

from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', productViewset)
router.register('customers', customerViewset)