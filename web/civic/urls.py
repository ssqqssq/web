from django.contrib import admin
from django.urls import path, include
from civil_talk import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name="home"),
    path('circulation_status', views.circulation_status, name="circulation_status"),
    path('about', views.about, name="about"),
    path('create', views.create, name="create"),
    path('users/', include('users.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
