from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TimestampedModel
import uuid
import datetime


class TimeStampListAPIView(APIView):

    def get(self, request):
        id = uuid.uuid4()
        time_stamps = str(datetime.datetime.now())
        stamps = TimestampedModel.objects.create(
            stamp_time_now=time_stamps, stamp_uuid_now=id)
        stamps.save()

        display_time_stamps = [
            items.stamp_time_now for items in TimestampedModel.objects.all()]
        display_uuid = [
            items.stamp_uuid_now for items in TimestampedModel.objects.all()]

        output = {display_time_stamps[i]: display_uuid[i]
                  for i in range(len(display_uuid))}

        return Response(output, status=status.HTTP_200_OK)
