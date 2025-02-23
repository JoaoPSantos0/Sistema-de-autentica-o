
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/',include('diario.urls')),
    path('register/',include('diario.urls'))
]
