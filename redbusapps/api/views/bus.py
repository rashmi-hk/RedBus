from rest_framework.response import Response
from rest_framework.views import APIView
from ...models import Bus
from ...serializers import BusSerializer
from django.core import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404
import json
# LOGGER = logging.getLogger(__name__)
from rest_framework import generics

class BusAPIList(APIView):

    # def get(self, request):
    #     print("inside bus get")
    #     try:
    #         get_data = Bus.objects.all()
    #         data = serializers.serialize('json', get_data)
    #         return_status = status.HTTP_200_OK
    #         # json.dumps  convert object to jsonstring
    #         return Response(data=json.dumps(data), status=return_status)
    #     except Bus.DoesNotExist:
    #
    #         bus = get_object_or_404(Bus)

    def post(self,request,):
        print("Inside post emp")
        user_dict = {}
        if 'id' in request.data:
            user_dict["id"] = request.data['id']
        if 'bus_name' in request.data:
            user_dict["bus_name"] = request.data['bus_name']
        if 'bus_number' in request.data:
            user_dict["bus_number"] = request.data['bus_number']
        if 'start_point' in request.data:
            user_dict["start_point"] = request.data['start_point']
        if 'destination' in request.data:
            user_dict["destination"] = request.data['destination']
        if 'arrival_time' in request.data:
            user_dict["arrival_time"] = request.data['arrival_time']
        if 'departure_time' in request.data:
            user_dict["departure_time"] = request.data['departure_time']
        if 'bus_image' in request.data:
            user_dict["bus_image"] = request.data['bus_image']



        serializer = BusSerializer(
            data=user_dict,
            partial=True
        )
        if serializer.is_valid(raise_exception=True):
           serializer.save()
        return_status = status.HTTP_200_OK
        return Response(data=user_dict,
                        status=return_status)

# class BusAPIList(generics.ListCreateAPIView):
#     permission_classes =
#     authentication_classes =
#     def get(self,request):
#         queryset = Bus.objects.all()
#         serializer_class = BusSerializer


    def get(self, request):
        print("inside bus get")
        try:
            get_data = Bus.objects.all()
            result_list = []
            for i in get_data:
                print("item", i.arrival_time)
                print("type", type(i.arrival_time))

                result_dict = {"id" : i.id,
                                "bus_name" : i.bus_name,
                                "bus_number": i.bus_number,
                                "start_point" : i.start_point,
                                "destination": i.destination ,
                                "arrival_time": str(i.arrival_time) ,
                                "departure_time":  str(i.departure_time) ,
                                "bus_image": str(i.bus_image) }
                result_list.append(result_dict)

            # data = serializers.serialize('json', get_data)
            return_status = status.HTTP_200_OK
            # # json.dumps  convert object to jsonstring
            return Response(data=json.dumps(result_list), status=return_status)
        except Bus.DoesNotExist:

            bus = get_object_or_404(Bus)

