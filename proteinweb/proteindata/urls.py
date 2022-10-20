from django.urls import include, path

from .import views
from .import api

urlpatterns = [
    path('', views.index, name='index'),
    path('proteinList/', views.proteinList, name='proteinList'),
    path('protein/<str:type>/', views.proteinDetail, name='protein'),
    
    path('pfamList/', views.pfamList.as_view(), name='pfamList'),
    path('pfam/<str:type>/', views.pfamDetail, name='pfam'),

    path('organismProteinList/', views.organismProteinList, name='organismProteinList'),
    path('organismPfamList/', views.organismPfamList, name='organismPfamList'),

    path('organismProtein/<str:type>/', views.organismProteinDetail, name='organismProtein'),
    path('organismPfam/<str:type>/', views.organismPfamDetail, name='organismPfam'),

    path('create_protein/', views.ProteinCreate.as_view(), name='create_protein'),

    path('api/protein/<str:type>/', api.protein_detail, name='protein_api'),
    path('api/pfam/<str:type>/', api.pfam_detail),

    path('api/proteins/<str:type>/', api.organismProtein_detail),
    path('api/pfams/<str:type>/', api.organismPfam_detail)    
]