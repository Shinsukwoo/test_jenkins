
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