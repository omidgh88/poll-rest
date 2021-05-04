from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.api_root),
    path('api-auth/', include('rest_framework.urls')),
    path('questions/', views.QuestionList.as_view(), name='question-list'),
    path('questions/<int:pk>', views.QuestionDetail.as_view(), name='question-detail'),
    path('choices/', views.ChoiceList.as_view(), name='choice-list'),
    path('choices/<int:pk>', views.ChoiceDetail.as_view(), name='choice-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
