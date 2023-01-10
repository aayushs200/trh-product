from django.urls import path
from app import views

urlpatterns = [
    # path('create_data/', views.CreateData.as_view(), name='trh')
    path('filter/', views.MongoData.as_view(), name='trh'),
    path('dropdown/', views.DropdownApi.as_view(), name='trh'),

]
