from django.urls import path
from . import views

app_name = 'loan_api'

urlpatterns = [
    path('', views.test),
    path('clients/', views.ClientViewAll.as_view()),
    path('clients/<int:pk>', views.ClientIdView.as_view()),
]
