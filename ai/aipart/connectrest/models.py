from django.db import models

# Create your models here.
class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):
        file_obj = request.FILES['file']
        # do some stuff with uploaded file
        return Response(status=204)