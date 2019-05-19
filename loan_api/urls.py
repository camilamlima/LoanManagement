from django.urls import path
from . import views

app_name = 'loan_api'

urlpatterns = [
    path('', views.test),
    path('clients/', views.ClientCreateView.as_view()),
    path('loans/', views.LoanCreateView.as_view()),
    path('loans/<int:loan_id>/payments/', views.PaymentCreateView.as_view()),
    path('loans/<int:loan_id>/balance/', views.BalanceView.as_view()),
]
