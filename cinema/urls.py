from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    GenreListCreateAPIView,
    GenreDetailAPIView,
    ActorListCreateAPIView,
    ActorDetailAPIView
)

app_name = "cinema"

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register(
    "cinema_halls",
    CinemaHallViewSet,
    basename="cinema_hall"
)

urlpatterns = [
    path(
        "genres/",
        GenreListCreateAPIView.as_view(),
        name="genre-list"
    ),
    path(
        "genres/<int:pk>/",
        GenreDetailAPIView.as_view(),
        name="genre-detail"
    ),

    path(
        "actors/",
        ActorListCreateAPIView.as_view(),
        name="actor-list"
    ),
    path(
        "actors/<int:pk>/",
        ActorDetailAPIView.as_view(),
        name="actor-detail"
    ),

    path("", include(router.urls)),
]
