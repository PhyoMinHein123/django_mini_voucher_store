from django.urls import path 
from myapp.views import index, detail, update, delete

urlpatterns = [
    path('', index),
    path('<int:id>/', detail),
    path('<int:id>/update/', update, name='voucher_update'),
    path('<int:id>/delete/', delete, name='voucher_delete'),
]