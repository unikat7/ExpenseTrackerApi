from django.urls import path,include
from expense_app.views import ExpenseView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'expenses', ExpenseView, basename='expense')

urlpatterns = [
    path('',include(router.urls))
]
