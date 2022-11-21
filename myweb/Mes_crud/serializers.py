from rest_framework import serializers
from .models import TbPlan , TbCustomer , TbOrder , TbItem , TbMaterial , TbProcess
from rest_framework.validators import UniqueValidator

class TbCustomersSerializer(serializers.ModelSerializer):       # 고객명, 고객코드
    class Meta:
        model = TbCustomer
        fields = ('customer_name','customer_code')

class TbOrdersSerializer(serializers.ModelSerializer):      # 수주코드 , 고객코드 , 제품코드, 수량, 수주날짜, 대표이름

    class Meta:
        model = TbOrder
        fields = ('order_code','customer_code','item_code','quantity','order_date','representative_name')

class TbItemsSerializer(serializers.ModelSerializer):       # 제품코드, 제품명

    class Meta:
        model = TbItem
        fields = ('item_code','item_name')

class TbPlansSerializer(serializers.ModelSerializer):       #Lot번호 , 수량 , 생산완료예정일 , 생산계획등록일 , 수주코드 , 제품코드

    class Meta:
        model = TbPlan
        fields = ('lot_num','quantity','due_date','reg_date','order_code','item_code')

class TbMaterialsSerializer(serializers.ModelSerializer):       # 원자재코드 , 원자재명 , 단위

    class Meta:
        model = TbMaterial
        fields = ('material_code','material_name','unit')

class TbProcessSerializer(serializers.ModelSerializer):         # 공정코드 , 공정명
    class Meta:
        model = TbProcess
        fields = ('process_code','process_name')

class TbPlanCreateSerializer(serializers.ModelSerializer):         # 생산계획 등록
    class Meta:
        model = TbPlan
        fields = ('lot_num','plan_name','quantity','due_date')
