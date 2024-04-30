from django.urls import path, include
from app import views

urlpatterns = [
    path("", views.index),
    path("api/", views.api),
    path(
        "api/",
        include(
            [
                path("projects", views.ProjectList.as_view()),
                path("projects/<int:id>/", views.ProjectDetail.as_view()),
            ]
        ),
    ),
]
