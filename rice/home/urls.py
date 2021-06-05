from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",views.index,name='home'),
    path("predictImage",views.predictImage,name="predictImage"),
    
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)