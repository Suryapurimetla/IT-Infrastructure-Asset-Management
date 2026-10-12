
from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Add asset
    path(
        'assets/add/',
        views.add_asset,
        name='add_asset',
    ),

    # Edit asset
    path(
        'assets/<int:asset_id>/edit/',
        views.edit_asset,
        name='edit_asset',
    ),

    # Delete asset
    path(
        'assets/<int:asset_id>/delete/',
        views.delete_asset,
        name='delete_asset',
    ),

    # Allocate asset
    path(
        'assets/<int:asset_id>/allocate/',
        views.allocate_asset,
        name='allocate_asset',
    ),

    # Asset maintenance
    path(
        'assets/<int:asset_id>/maintenance/',
        views.maintain_asset,
        name='maintain_asset',
    ),
]
