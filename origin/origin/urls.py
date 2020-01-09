from django.contrib import admin
from django.urls import path

from bonds.views import HelloWorld, BondViewSet

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HelloWorld.as_view()),
    path("bonds/", BondViewSet.as_view({"get": "list", "post": "create"}))
]
