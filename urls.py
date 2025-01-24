from django.urls import path
from .views import RegisterView, LoginView, UserBalanceView, AddBalanceView, TransferView, TransferListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('balance/', UserBalanceView.as_view(), name='user_balance'),
    path('add-balance/', AddBalanceView.as_view(), name='add_balance'),
    path('transfer/', TransferView.as_view(), name='transfer'),
    path('transfers/', TransferListView.as_view(), name='transfer_list'),
]