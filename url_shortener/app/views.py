from django.shortcuts import redirect
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response

from .Logic import url_logic
from .serializer import UrlPostSerializer, UrlResponseSerializer


class UrlController(viewsets.ViewSet):
    def redirect(self, request: Request, id: str):
        try:
            response = url_logic.get_short_url(url=id)
            return redirect(response)
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)

    def post(self, request: Request):
        try:
            serializer = UrlPostSerializer(data=request.data)
            if serializer.is_valid():
                long_url = serializer.validated_data.get("long_url")
                response = url_logic.add_long_url(long_url=long_url)
                serialized_response = UrlResponseSerializer(response)
                return Response(data=serialized_response.data, status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)
