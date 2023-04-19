from rest_framework import serializers
from .models import TbPlan , TbCustomer , TbOrder , TbItem , TbMaterial , TbProcess, TbProductionLog, TbNotice, TbMachine,TbStaff, TbAuthorGroup
from rest_framework.validators import UniqueValidator

class TbCustomersSerializer(serializers.ModelSerializer):       # 고객명, 고객코드
    class Meta:
        model = TbCustomer
        fields = ('customer_name','customer_code','reg_id', 'mod_id', 'homepage', 'customer_phone', 'representative_phone', 'representative_name', 'reg_date', 'mod_date')

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
        # fields = ('lot_num','quantity','due_date','reg_date','order_code','item_code')
        fields = ('flag','lot_num','order_code','item_code','quantity','due_date','reg_date','reg_id','mod_date','mod_id','plan_name')

class TbMaterialsSerializer(serializers.ModelSerializer):       # 원자재코드 , 원자재명 , 단위

    class Meta:
        model = TbMaterial
        fields = ('material_code','material_name','unit')

class TbProcessSerializer(serializers.ModelSerializer):         # 공정코드 , 공정명

    class Meta:
        model = TbProcess
        fields = ('process_code','process_name')

class TbPlanCreateSerializer(serializers.ModelSerializer):         # 생산계획(계획) 등록 , 수정 ,삭제

    class Meta:
        model = TbPlan
        # fields = '__all__'
        fields = ('flag','lot_num','item_code','quantity','due_date','plan_name')

class TbPlanOrderCreateSerializer(serializers.ModelSerializer):         # 생산계획(수주) 등록 수정 , 삭제 

    class Meta:
        model = TbPlan  
        fields = ('flag','lot_num','order_code','item_code','quantity','due_date','plan_name')
class TbTest(serializers.ModelSerializer):
    class Meta:
        model = TbPlan
        fields = ('order_code', 'lot_num')

## 생산 데이터
class TbproductionlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbProductionLog
        fields = ('curdatetime','linecode','metalgoodcnt', 'metalbadcnt', 'weightgoodcnt', 'weighthighcnt', 'weightlowcnt')

# 공지사항 정보
class TbnoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbNotice
        fields = ('id','notice_subject', 'notice_content', 'reg_date', 'reg_id')

# 설비 정보
class TbMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbMachine
        fields = ('machine_code','machine_name','line_name','manager_main','reg_date','reg_id','mod_date','mod_id')


class TbAuthorGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbAuthorGroup
        fields = ('author_id','author_name')

# 사원정보
class TbStaffSerializer(serializers.ModelSerializer):
    # group = TbAuthorGroupSerializer(many = True, read_only = True)
    class Meta:
        model = TbStaff
        fields = ('author','name','id','password','department','position','phone_num','email_addr','status', 'reg_date','reg_id','mod_date','mod_id')

    # def to_representation(self, instance):
    #     self.fields['author_id'] = TbAuthorGroupSerializer()
    #     return super(TbStaffSerializer, self).to_representation(instance)