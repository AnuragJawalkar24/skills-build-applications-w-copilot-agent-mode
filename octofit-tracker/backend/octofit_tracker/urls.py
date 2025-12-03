
import os
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from octofit_tracker import views

@api_view(['GET'])
def api_root(request, format=None):
    codespace_name = os.environ.get('CODESPACE_NAME', '')
    base_url = f"https://{codespace_name}-8000.app.github.dev/api/" if codespace_name else request.build_absolute_uri('api/')
    return Response({
        'users': f"{base_url}users/",
        'teams': f"{base_url}teams/",
        'activities': f"{base_url}activities/",
        'workouts': f"{base_url}workouts/",
        'leaderboard': f"{base_url}leaderboard/",
    })
    
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.api_root, name='api-root'),
    path('api/', include(router.urls)),
]
## ...existing code above...
