from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *


# Create your views here.
class DocumentView(ModelViewSet):
    queryset = Document.objects.order_by('pk')
    serializer_class = DocumentSerializer


class QuestionView(ModelViewSet):
    queryset = Question.objects.order_by('pk')
    serializer_class = QuestionSerializer


class AnswerView(ModelViewSet):
    queryset = Answer.objects.order_by('pk')
    serializer_class = AnswerSerializer
