from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import NIDSerializer
from .services import NIDService


class NationalIdViewSet(viewsets.ViewSet):

    @action(methods=['POST'], detail=False)
    def extract_national_id_information(self, request, *args, **kwargs) -> Response:
        # TODO roa2 hena, enna n7ot el serializer fo2
        serializer = NIDSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        service_national_id = NIDService(
            nid=serializer.validated_data["national_id"])
        extracted_data = service_national_id.get_national_id_information()

        return Response(extracted_data, status=status.HTTP_200_OK)
