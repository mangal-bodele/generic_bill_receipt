from django.urls import path
from .views import *

urlpatterns = [
    path('create/', Bill_Create.as_view(),name="create_url"),
    path('list/', Bill_List.as_view(),name="list_url"),
    path('detail/<int:pk>/', Bill_Detail.as_view(),name="detail_url"),
    path('update/<int:pk>/', Bill_Update.as_view(),name="update_url"),
    path('delete/<int:pk>/', Bill_Delete.as_view(),name="delete_url")
]