
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('assets/add/', views.add_asset, name='add_asset'),

    path('assets/<int:asset_id>/edit/', views.edit_asset, name='edit_asset'),

    path('assets/<int:asset_id>/delete/', views.delete_asset, name='delete_asset'),

    path('assets/<int:asset_id>/allocate/', views.allocate_asset, name='allocate_asset'),

    path('assets/<int:asset_id>/maintenance/', views.maintain_asset, name='maintain_asset'),

    path('assets/<int:asset_id>/history/', views.maintenance_history, name='maintenance_history'),

    path('assets/<int:asset_id>/allocation-history/', views.allocation_history, name='allocation_history'),

    path(
    'assets/<int:asset_id>/return/',
    views.return_asset,
    name='return_asset'
),

]
