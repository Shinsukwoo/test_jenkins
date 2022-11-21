from django.urls import path
from .views import TbPlansAPIView , TbCustomersAPIView, TbItemsAPIView , TbOrdersAPIView, TbMaterialsAPIView , TbProcessAPIView
from .views import TbPlanAPIView

urlpatterns = [
    path('plans/', TbPlansAPIView.as_view()),
    path('plan/<int:pk>/', TbPlanAPIView.as_view()),
    path('customers/', TbCustomersAPIView.as_view()),
    path('items/', TbItemsAPIView.as_view()),
    path('orders/', TbOrdersAPIView.as_view()),
    path('materials/', TbMaterialsAPIView.as_view()),
    path('process/', TbProcessAPIView.as_view()),
]