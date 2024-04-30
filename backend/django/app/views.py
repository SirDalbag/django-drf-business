from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from app import models, serializers


def index(request: HttpRequest) -> HttpResponse:
    """
    HTML rendering.

        Parameters:
            request (HttpRequest): The request object.

        Returns:
            (HttpResponse): HTML code.
    """

    try:
        return render(request, "index.html")
    except Exception as error:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)


@api_view(http_method_names=["GET", "POST", "PUT", "DELETE"])
@permission_classes([AllowAny])
def api(request: Request) -> Response:
    """
    Testing a request.

        Parameters:
            request (Request): The request object.

        Returns:
            If successful:
                (Response): JSON object with request status 200 OK and HTTP method.
            If unsuccessful:
                (Response): JSON object with request status 400 Bad Request and error message.
    """

    try:
        return Response(
            data={"message": "OK", "method": request.method}, status=status.HTTP_200_OK
        )
    except Exception as error:
        return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)


class ProjectList(APIView):
    """
    Receive all projects or create a new project.

        Permissions:
            Authenticated users only.

        Methods:
            GET: Get a list of all active projects.
            POST: Create a new project.

        Parameters:
            authors (str): Comma-separated list of usernames.
            category (str): Category slug.
            tags (str): Comma-separated list of tags slugs.
            title (str): Project title.
            description (str): Project description.
            images (str): Comma-separated list of image URLs.
            files (str): Comma-separated list of file URLs.

        Returns:
            If successful:
                [GET] (Response): JSON object with request status 200 OK and list of projects.
                [POST] (Response): JSON object with request status 201 Created and new project.
            If unsuccessful:
                (Response): JSON object with request status 400 Bad Request and error message.

    """

    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        """
        Get a list of all active projects.

            Parameters:
                request (Request): The request object.

            Returns:
                If successful:
                    (Response): JSON object with request status 200 OK and list of projects.
                If unsuccessful:
                    (Response): JSON object with request status 400 Bad Request and error message.
        """

        try:
            projects = models.Project.objects.filter(is_active=True)
            serializer = serializers.ProjectSerializer(projects, many=True)
            return Response(data={"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request: Request) -> Response:
        """
        Create a new project.

            Parameters:
                authors (str): Comma-separated list of usernames.
                category (str): Category slug.
                tags (str): Comma-separated list of tags slugs.
                title (str): Project title.
                description (str): Project description.
                images (str): Comma-separated list of image URLs.
                files (str): Comma-separated list of file URLs.

            Returns:
                If successful:
                    (Response): JSON object with request status 201 Created and new project.
                If unsuccessful:
                    (Response): JSON object with request status 400 Bad Request and error message.
        """

        try:
            title = request.POST.get("title", None)
            description = request.POST.get("description", None)
            category_slug = request.POST.get("category", None)
            if category:
                category = models.Category.objects.get(slug=category_slug)
            project = models.Project.objects.create(
                title=title,
                description=description,
                category=category,
            )
            authors = request.POST.get("authors", None)
            if authors:
                users = User.objects.filter(username__in=authors.split(","))
                project.authors.set(users)
            tags_slugs = request.POST.get("tags", None)
            if tags_slugs:
                tags = models.Tag.objects.filter(slug__in=tags_slugs.split(","))
                project.tags.set(tags)
            images_urls = request.POST.get("images", None)
            if images_urls:
                images = models.Image.objects.bulk_create(
                    [models.Image(url=url) for url in images_urls.split(",")]
                )
                project.images.set(images)
            files_urls = request.POST.get("files", None)
            if files_urls:
                files = models.File.objects.bulk_create(
                    [models.File(url=url) for url in files_urls.split(",")]
                )
                project.files.set(files)
            serializer = serializers.ProjectSerializer(project, many=False)
            return Response(
                data={"data": serializer.data}, status=status.HTTP_201_CREATED
            )
        except Exception as error:
            return Response(
                data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST
            )
