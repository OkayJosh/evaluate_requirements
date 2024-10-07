import os

from django.conf import settings
from rest_framework import serializers

class EvaluationSerializer(serializers.Serializer):
    filename = serializers.FileField()

    def save(self):
        # Get the uploaded file instance from the validated data
        uploaded_file = self.validated_data['filename']

        # Extract the file name from the uploaded file
        file_name = uploaded_file.name

        # Ensure that MEDIA_ROOT exists
        if not os.path.exists(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)

        # Build the file path where the file will be saved
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)

        # Open the file in binary mode to handle any kind of file
        with open(file_path, 'wb+') as destination:
            # Write the file chunks to the destination
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Return the filename and file path
        return {
            "filename": file_name,
            "filepath": file_path,
        }