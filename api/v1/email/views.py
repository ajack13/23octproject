import os
import re
import json
import time
import random
import traceback
from uuid import uuid4
from datetime import datetime
from django.db.models import Q
from api.models import Email

from django.conf import settings
from django.core.cache import cache
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, Http404, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseServerError
from rest_framework import filters
from rest_framework import parsers
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from . import helpers

import logging
logger = logging.getLogger('interview')

class SendEmail(GenericAPIView):
    #     """
    #     This endpoint is used to send email.
    #     """
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.EmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() is False:
            logger.error('Email api bad request')
            return Response({"status": False, "message": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data
        logger.info('Bulk Email API in progress')
        new_email = Email()
        try:
            helpers.send_email(data)
            new_email.status = 'success'
            logger.debug('Email sent, id : ' + str(new_email.id))
            new_email.save()
            return Response({"status": True, "message": "Email Sent Successfully !"}, status=200)
        except:
            new_email.status = 'fail'
            new_email.save()
            logger.error('Email failed, id : ' + str(new_email.id))
            return Response({"status": True, "message": "Email Not Sent!"}, status=500)


class BulkEmailUpload(GenericAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.FileUploadSerializer
    parser_classes = (parsers.MultiPartParser,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        files = request.FILES.getlist('file')
        if serializer.is_valid() is False:
            logger.error('Email bulk api bad request')
            return Response({"status": False, "message": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data
        logger.info('Bulk Email API in progress')

        folder_name =  str(uuid4().hex) + str(int(time.time()))
        for i, file in enumerate(files):
            original_file_name = file.name
            renamed_file_name = str(i) + '.csv'

            file.name = renamed_file_name

            custom_path = os.path.join(folder_name, renamed_file_name)
            file_location = f'{settings.ARCHIVE_DIR}/{custom_path}'

            fs = FileSystemStorage()
            logger.info('File upload successfull')

            filename = fs.save(file_location, file)
            uploaded_file_url = fs.url(filename)

            try:
                emails = helpers.import_email_csv(file_location)
            except:
                logger.error('CSV parsing failed' + str(traceback.format_exc()))
                return Response({"status": False, "message": "CSV file parsing failed!"}, status=500)

            logger.info('Email ids in file ' + str(emails))
            bulk_email_params = {"to": emails['to'], "cc": emails['cc'], "bcc": emails['bcc'],
                                 "from": data["from_email"],
                                 "subject": data["subject"],
                                 "body": data["body"]}
            

            try:
                helpers.send_email(bulk_email_params)
            except:
                logger.error('Email upload failed' + str(traceback.format_exc()))
                return Response({"status": False, "message": "Email file uploaded failed !"}, status=500)


        return Response({"status": True, "message": "Email file uploaded Successfully !"}, status=200)
