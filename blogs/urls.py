from rest_framework.routers import SimpleRouter
from blogs import views

router = SimpleRouter()

router.register(r'document',views.DocumentView)
router.register(r'question',views.QuestionView)
router.register(r'answer',views.AnswerView)

urlpatterns = router.urls