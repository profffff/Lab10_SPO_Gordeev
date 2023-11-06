from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('login/', views.LoginView.as_view(), name='login'),
    path('', lambda request: redirect('/login/')),
    path('', include('account.urls'), name='login')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


