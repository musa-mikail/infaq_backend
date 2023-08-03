from django.urls import path
from . import views

urlpatterns = [
    path('', views.MosqueListAPIView.as_view(), name='mosque_list'),
    path('<int:id>/', views.MosqueDetailAPIView.as_view(), name='mosque_details'),
    path('create/', views.MosqueCreateAPIView.as_view(), name='mosque_create'),
    path('update/<int:id>/', views.MosqueRetrieveUpdateView.as_view(), name='mosque_update'),
    path('delete/<int:id>/', views.MosqueDestroyAPIView.as_view(), name='mosque_delete'),
]