from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Choice, Question
from .permissions import IsOwnerOrReadOnly
from .serializers import ChoiceSerializer, QuestionSerializer, UserSerializer


class QuestionViewset(viewsets.ModelViewSet):
    """This viewset automatically provides 
    `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChoiceList(generics.ListCreateAPIView):
    """list all Choices or generate new one
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    """retrieve, update or delete an instance
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """ This viewset automatically provides 'list' and 'retrieve' actions
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'questions': reverse('question-list', request=request, format=format),
    })
