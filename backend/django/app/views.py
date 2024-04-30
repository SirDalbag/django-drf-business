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
            projects = models.Project.objects.all()
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
                request (Request): The request object.
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
            tag_slugs = request.POST.get("tags", None)
            if tag_slugs:
                tags = models.Tag.objects.filter(slug__in=tag_slugs.split(","))
                project.tags.set(tags)
            image_urls = request.POST.get("images", None)
            if image_urls:
                images = models.Image.objects.bulk_create(
                    [models.Image(url=url) for url in image_urls.split(",")]
                )
                project.images.set(images)
            file_urls = request.POST.get("files", None)
            if file_urls:
                files = models.File.objects.bulk_create(
                    [models.File(url=url) for url in file_urls.split(",")]
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


class ProjectDetail(APIView):
    """
    Receive the project, update it, or delete it.

        Permissions:
            Authenticated users only.

        Methods:
            GET: Get the project.
            PUT: Update the project.
            DELETE: Delete the project.

        Parameters:
            id (int): Project id.
            authors (str): Comma-separated list of usernames.
            category (str): Category slug.
            tags (str): Comma-separated list of tags slugs.
            title (str): Project title.
            description (str): Project description.
            images (str): Comma-separated list of image URLs.
            files (str): Comma-separated list of file URLs.

        Returns:
            If successful:
                [GET] (Response): JSON object with request status 200 OK and project.
                [PUT] (Response): JSON object with request status 200 OK and updated project.
                [DELETE] (Response): JSON object with request status 204 No Content.
            If unsuccessful:
                (Response): JSON object with request status 400 Bad Request and error message.
    """

    permission_classes = [IsAuthenticated]

    def get_object(self, id: int) -> models.Project:
        """
        Get the project.

            Parameters:
                id (int): Project id.

            Returns:
                (models.Project): Project object.
        """

        try:
            return models.Project.objects.get(id=id)
        except Exception as error:
            raise models.Project.DoesNotExist()

    def get(self, request: Request, id: int) -> Response:
        """
        Get the project.

            Parameters:
                request (Request): The request object.
                id (int): Project id.

            Returns:
                If successful:
                    (Response): JSON object with request status 200 OK and project.
                If unsuccessful:
                    (Response): JSON object with request status 400 Bad Request and error message.
        """

        try:
            project = self.get_object(id)
            serializer = serializers.ProjectSerializer(project, many=False)
            return Response(data={"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request: Request, id: int) -> Response:
        """
        Update the project.

            Parameters:
                request (Request): The request object.
                id (int): Project id.
                authors (str): Comma-separated list of usernames.
                category (str): Category slug.
                tags (str): Comma-separated list of tags slugs.
                title (str): Project title.
                description (str): Project description.
                images (str): Comma-separated list of image URLs.
                files (str): Comma-separated list of file URLs.

            Returns:
                If successful:
                    (Response): JSON object with request status 200 OK and updated project.
                If unsuccessful:
                    (Response): JSON object with request status 400 Bad Request and error message.
        """

        try:
            project = self.get_object(id)
            title = request.POST.get("title", None)
            if title and project.title != title:
                project.title = title
            description = request.POST.get("description", None)
            if project.description != description:
                project.description = description
            category_slug = request.POST.get("category", None)
            if category:
                category = models.Category.objects.get(slug=category_slug)
            if project.category != category:
                project.category = category
            tag_slugs = request.POST.get("tags", None)
            if tag_slugs:
                tags = models.Tag.objects.filter(slug__in=tag_slugs.split(","))
            if project.tags != tags:
                project.tags = tags
            project.save()
            serializer = serializers.ProjectSerializer(project, many=False)
            return Response(data={"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request: Request, id: int) -> Response:
        """
        Delete the project.

            Parameters:
                request (Request): The request object.
                id (int): Project id.

            Returns:
                If successful:
                    (Response): JSON object with request status 204 No Content.
                If unsuccessful:
                    (Response): JSON object with request status 400 Bad Request and error message.
        """

        try:
            project = self.get_object(id)
            project.is_active = False
            project.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(
                data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST
            )
