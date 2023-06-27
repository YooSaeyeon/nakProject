from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('about/', include('about.urls'), name='about'),
    path('apply/', include('apply.urls'), name='apply'),
    path('songRequest/', include('songRequest.urls'), name='songRequest'),
    path('blog/', include('blog.urls'), name='blog'),
    path('notice/', include('notice.urls'), name='notice'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('authaccounts/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)