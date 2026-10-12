
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django administration panel
    path('admin/', admin.site.urls),

    # ITAM application dashboard and asset management
    path('', include('assets.urls')),
]
