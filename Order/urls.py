from rest_framework.routers import SimpleRouter
from Order import views

router = SimpleRouter()

router.register(r'basket', views.BasketView)
router.register(r'payment', views.PaymentView)
router.register(r'FavoriteProduct', views.FavoriteProductView)

urlpatterns = router.urls
