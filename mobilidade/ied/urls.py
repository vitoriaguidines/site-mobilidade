from django.urls import path
from django.urls import path
from ied import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('friends/', views.friends_view, name='friends')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)