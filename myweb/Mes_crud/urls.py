from django.urls import path
from .views import TbPlansAPIView , TbCustomersAPIView, TbItemsAPIView , TbOrdersAPIView, TbMaterialsAPIView , TbProcessAPIView
from .views import TbPlanAPIView , TbPlanOrderCreateAPIView , TbPlanOrderRUDAPIView

urlpatterns = [
    path('plans/', TbPlansAPIView.as_view()),
    path('plan/<str:lot_num>/', TbPlanAPIView.as_view()),
    path('customers/', TbCustomersAPIView.as_view()),
    path('items/', TbItemsAPIView.as_view()),
    path('orders/', TbOrdersAPIView.as_view()),
    path('materials/', TbMaterialsAPIView.as_view()),
    path('process/', TbProcessAPIView.as_view()),
    path('create_order/', TbPlanOrderCreateAPIView.as_view()),
    path('order/<str:lot_num>/', TbPlanOrderRUDAPIView.as_view()),
]