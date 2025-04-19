from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog import views


router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')

urlpatterns = [
    # path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetails.as_view(), name='post_detail'),
    path('api/v1/', include(router.urls))
]