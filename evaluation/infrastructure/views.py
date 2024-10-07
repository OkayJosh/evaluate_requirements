import os

from django.conf import settings
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from evaluation.application.services import EvaluationService
from evaluation.infrastructure.serializers import EvaluationSerializer


class EvaluationView(APIView):
    """
    Evaluation view
    """
    parser_classes = (MultiPartParser,)

    def post(self, request):
        """
        Post request for processing file
        :param request:
        :return:
        """
        serializer = EvaluationSerializer(data=request.data)
        if serializer.is_valid():
            uploaded_file_details = serializer.save()

            # Load the CSV file and perform evaluation
            evaluation_service = EvaluationService(**uploaded_file_details)
            minimum_requirements = evaluation_service.evaluate()
            return Response(evaluation_service.output_results(minimum_requirements, output_as_json=True),
                            status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
