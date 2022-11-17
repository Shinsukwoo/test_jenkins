from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import * # 수정해야됨
from .models import * # 수정해야됨
from rest_framework.generics import get_object_or_404
from django.contrib.auth.decorators import login_required
from . import serializers
# Create your views here.
# 생산계획관리

# 생산계획관리 - 검색



# 생산계획관리 - 등록

########################## 
# 생산계획관리 - 테이블tb_plan(LoT번호, 수주코드, 수량, 생산완료날짜, 생산계획등록일)tb_order(제품명, 고객명)
class Produce_Plan(APIView):
    def get(self, request, format=None):
        questions_plan = tb_plan.objects.only("lot_num","order_code", "quantity","due_data", "reg_date")
        questions_name = tb_customer.objects.only("customer_name")
        questions_name1 = tb_item.objects.only("item_name")
        questions_plan[0:2]+ questions_name + questions_plan[2:]