from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('questions', views.QuestionViewset)
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('choices/', views.ChoiceList.as_view(), name='choice-list'),
    path('choices/<int:pk>', views.ChoiceDetail.as_view(), name='choice-detail'),
]
