from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from .serializers import TbPlansSerializer , TbCustomersSerializer , TbItemsSerializer , TbOrdersSerializer, TbMaterialsSerializer
from .serializers import TbProcessSerializer, TbPlanCreateSerializer 
from .models import TbPlan , TbCustomer , TbItem , TbOrder , TbMaterial , TbProcess
# Create your views here.

class TbPlansAPIView(APIView):      # 생산계획조회 API
    def get(self, request):
        plans = TbPlan.objects.all()
        serializer = TbPlansSerializer(plans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # def post(self, request):
    #     serializer = TbPlanCreateSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TbPlanAPIView(APIView):
    def get(self, request, pk):
        plan = get_object_or_404(TbPlan, id=pk)
        serializer = TbPlanCreateSerializer(plan)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # def put(self, request, pk):
    #     plan = get_object_or_404(TbPlan, id=pk)
    #     serializer = TbPlanCreateSerializer(plan, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TbOrdersAPIView(APIView):     # 수주조회 API
    def get(self, request):
        orders = TbOrder.objects.all()
        serializer = TbOrdersSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TbCustomersAPIView(APIView):      # 고객조회 API
    def get(self, request):
        customers = TbCustomer.objects.all()
        serializer = TbCustomersSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TbItemsAPIView(APIView):      # 제품조회 API
    def get(self, request):
        items = TbItem.objects.all()
        serializer = TbItemsSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TbMaterialsAPIView(APIView):      # 원자재조회 API
    def get(self, request):
        materials = TbMaterial.objects.all()
        serializer = TbMaterialsSerializer(materials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TbProcessAPIView(APIView):        # 공정조회 API
    def get(self, request):
        process = TbProcess.objects.all()
        serializer = TbProcessSerializer(process, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
