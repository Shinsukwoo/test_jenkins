from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics , mixins
from django.shortcuts  import get_object_or_404
from .serializers import TbPlansSerializer , TbCustomersSerializer , TbItemsSerializer , TbOrdersSerializer, TbMaterialsSerializer
from .serializers import TbProcessSerializer, TbPlanCreateSerializer, TbPlanOrderCreateSerializer , TbTest, TbproductionlogSerializer, TbnoticeSerializer, TbMachineSerializer,TbStaffSerializer,TbAuthorGroupSerializer
from .models import TbPlan , TbCustomer , TbItem , TbOrder , TbMaterial , TbProcess, TbProductionLog, TbNotice, TbMachine, TbStaff, TbAuthorGroup
from rest_framework.parsers import JSONParser
from django.http import Http404
# Create your views here.
def index(request):
    return render(request, "demo_app/index.html")

class TbPlansAPIView(APIView):      # 생산 계획 조회, 등록(계획) API 
    def get(self, request):
        plans = TbPlan.objects.all()
        serializer = TbPlansSerializer(plans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = TbPlanCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TbPlanOrderCreateAPIView(APIView):       # 생산 계획 등록(수주) API
    def post(self, request):
        serializer = TbPlanOrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TbPlanAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TbPlan.objects.filter(flag='P')
    serializer_class = TbPlanCreateSerializer
    lookup_field = 'lot_num'

class TbPlanOrderRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TbPlan.objects.filter(flag='O')
    serializer_class = TbPlanOrderCreateSerializer
    lookup_field = 'lot_num'


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
    def post(self, request):
        serializer = TbCustomersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

class TbPlanTestAPIView(APIView):
    def get(self, request):
        plan = TbPlan.objects.all()
        serializer = TbTest(plan, many=True)
        for ordercode in serializer.data:
            print(ordercode.order_code)
            print(ordercode.lot_num)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TbproductionlogAPIView(APIView):      # 모니터링 API
    def get(self, request):
        productionlog = TbProductionLog.objects.all()
        serializer = TbproductionlogSerializer(productionlog, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

# @csrf_exempt
class TbnoticeAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(TbNotice, pk=pk)
    def get(self, request,pk):
        notice = self.get_object(pk)
        serializer = TbnoticeSerializer(notice)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = TbnoticeSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_200_OK)



class TbnoticelistAPIView(APIView):
    def get(self, request,format=None):
        notice = TbNotice.objects.all()
        serializer = TbnoticeSerializer(notice, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = TbnoticeSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer._validated_data.get('notice_subject'))
            # print(serializer.data('notice_subject'))
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class TbMachineAPIView(APIView):
    def get(self, request):
        notice = TbMachine.objects.all()
        serializer = TbMachineSerializer(notice, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = TbMachineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TbStaffAPIView(APIView):

    def get(self, request):
        notice = TbStaff.objects.all()
        serializer = TbStaffSerializer(notice, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = TbStaffSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer._validated_data)
            # print(serializer.data('notice_subject'))
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TbAuthorGroupAPIView(APIView):
  def get(self, request):
        notice = TbAuthorGroup.objects.all()
        serializer = TbAuthorGroupSerializer(notice, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


public_post_detail = TbnoticeAPIView.as_view()