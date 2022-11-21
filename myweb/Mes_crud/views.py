<<<<<<< HEAD
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
=======

# Create your views here.
############################################ 생산계획관리

# 생산계획관리 - 검색



# 생산계획관리 - 등록

########################## 
# 생산계획관리 - 테이블tb_plan(LoT번호, 수주코드, 수량, 생산완료날짜, 생산계획등록일)tb_order(제품명, 고객명)
# tbplan 테이블 전체 가져오기
class TbPlanAPI(generics.ListAPIView):
        questions = TbPlan.objects.all()      
        serializer_class = TbPlanSerializer

# tbcustomer 테이블 전체 가져오기
class CustomerAPI(generics.ListAPIView):
        questions = TbCustomer.objects.all()
        serializer_class = CustomerSerializer
    
# tbitem 테이블 전체 가져오기
class TbItemAPI(generics.ListAPIView):       
        questions = TbItem.objects.all()
        serializer_class = TbItemSerializer
>>>>>>> b1ceafcee0b690a16c29cc278b395c92f6ab7a2a
