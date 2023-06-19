from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData, name='getData'),
    path('api/total_items', views.total_items, name='api/total_items'),
    path('api/nth_most_total_item', views.nth_most_total_item, name='api/nth_most_total_item'),
    path('api/percentage_of_department_wise_sold_items', views.get_percent, name='api/percentage_of_department_wise_sold_items'),
    path('api/monthly_sales', views.monthly_sales, name='api/monthly_sales'),
]