from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),    
    path('guitars/', views.guitars_index, name='index'),
    path('guitars/<int:guitar_id>/', views.guitars_detail, name='detail'),
    path('guitars/create/', views.GuitarCreate.as_view(), name='guitars_create'),
    path('guitars/<int:pk>/update/', views.GuitarUpdate.as_view(), name='guitars_update'),
    path('guitars/<int:pk>/delete/', views.GuitarDelete.as_view(), name='guitars_delete'),
    path('accessories/create', views.AccessoryCreate.as_view(), name='accessories_create'),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
    path('accessories/<int:pk>/delete', views.AccessoryDelete.as_view(), name='accessories_delete'),
    path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
    path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessories_update'),
    path('guitars/<int:guitar_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),

]   
