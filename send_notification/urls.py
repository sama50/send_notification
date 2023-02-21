from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import home , upload_video

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="home"),
    path('<int:id>/',upload_video, name="post"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
