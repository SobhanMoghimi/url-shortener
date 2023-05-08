from django.shortcuts import redirect
from pydantic import json
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response

from .Logic import url_logic
from .Logic.dto import LongUrlDto


class UrlController(viewsets.ViewSet):
    def redirect(self, request: Request, short_url: str):
        try:
            response = url_logic.get_short_url(url=short_url)
            return redirect(response)
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)

    def post(self, request: Request):
        try:
            response = url_logic.add_long_url(long_url_dto=LongUrlDto(**request.data))
            return Response(data=response.dict(), status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)
