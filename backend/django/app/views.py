from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


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
        return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(http_method_names=["GET", "POST", "PUT", "DELETE"])
@permission_classes([AllowAny])
def api(request: Request) -> Response:
    """
    Testing a request.

        Parameters:
            request (Request): The request object.

        Returns:
            (Response): JSON object with request status and HTTP method.
    """

    try:
        return Response(
            data={"message": "OK", "method": request.method}, status=status.HTTP_200_OK
        )
    except Exception as error:
        return Response(
            data={"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
