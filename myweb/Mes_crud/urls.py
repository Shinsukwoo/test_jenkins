from django.urls import path
from .views import TbPlansAPIView , TbCustomersAPIView, TbItemsAPIView , TbOrdersAPIView, TbMaterialsAPIView , TbProcessAPIView
from .views import TbPlanAPIView , TbPlanOrderCreateAPIView , TbPlanOrderRUDAPIView , TbPlanTestAPIView , TbProductionLogAPIView

urlpatterns = [
    path('plans/', TbPlansAPIView.as_view()),       # 전체 조회, 등록(계획) 
    path('plan/<str:lot_num>/', TbPlanAPIView.as_view()),       # 수정 (계획)
    path('customers/', TbCustomersAPIView.as_view()),       # 고객명 , 고객코드       
    path('items/', TbItemsAPIView.as_view()),       # 제품코드, 제품명
    path('orders/', TbOrdersAPIView.as_view()),     # 수주관리
    path('materials/', TbMaterialsAPIView.as_view()),       # 원자재코드, 단위, 원자재명
    path('process/', TbProcessAPIView.as_view()),       #  공정코드 , 공정명
    path('create_order/', TbPlanOrderCreateAPIView.as_view()),      # 등록(수주)
    path('order/<str:lot_num>/', TbPlanOrderRUDAPIView.as_view()),      # 수정 (수주)
    path('test/plan/', TbPlanTestAPIView.as_view()),
    path('productionlog/', TbProductionLogAPIView.as_view()),
]