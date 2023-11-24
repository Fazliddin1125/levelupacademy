from django.shortcuts import render
from rest_framework.views import APIView
from main.models import Customer, Course
from .serializers import CustomerSerializers, CourseSerailizers
from rest_framework.response import Response
from rest_framework import generics, status


class CostumerListView(APIView):
    def get(self, request):
        try:
            customers = Customer.objects.all()
            serializer_data = CustomerSerializers(customers, many=True).data
            data = {
                'status': True,
                'customers': serializer_data,
                'message': f"Return {len(customers)}"
            }

            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    "message": 'Not found',
                    status: False
                }, status=status.HTTP_404_NOT_FOUND
            )

class CourseApiView(APIView):
    def get(self, requset):
        try:
            course = Course.objects.all()
            serializer_data = CourseSerailizers(course, many=True).data
            data = {
                'status': True,
                'customers': serializer_data,
                'message': f"Return {len(course)}"
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    "message": 'Not found',
                    status: False
                }, status=status.HTTP_404_NOT_FOUND
            )
