from rest_framework.routers import SimpleRouter
from Order import views

router = SimpleRouter()

router.register(r'basket', views.BasketView)
router.register(r'payment', views.PaymentView)
urlpatterns = router.urls
