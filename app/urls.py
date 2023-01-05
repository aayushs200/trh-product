from django.urls import path
from app import views

urlpatterns = [
    path('filter/', views.MongoData.as_view(), name='trh'),
    # path('create_data/', views.CreateData.as_view(), name='trh')
]
