from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('account/', include('account.urls')),
    path('client/', include('client.urls')),
    path('writer/', include('writer.urls')),
]
