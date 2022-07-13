from rest_framework.decorators import action
from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import NIDSerializer
from .services import NIDService


class NationalIdViewSet(viewsets.ViewSet):

    @action(methods=['POST'], detail=False, url_path="data/")
    def extract_national_id_information(self, request, *args, **kwargs) -> Response:
        serializer = NIDSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        service_national_id = NIDService()
        extracted_data = service_national_id.get_national_id_information(
            nid=serializer.validated_data["national_id"])

        return Response(extracted_data.__dict__, status=status.HTTP_200_OK)
