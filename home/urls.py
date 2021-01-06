
from django.contrib import admin
from django.urls import path
from crawler.views import hello_world

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/<str:query>', hello_world),

]
