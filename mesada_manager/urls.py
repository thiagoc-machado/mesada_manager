
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("login.urls")),
    path('kids/', include("kids.urls")),
    path('parents/', include("parents.urls")),
    path('users/', include("users.urls")),
 ]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# def handle_404(request, exception):
#     return redirect('dashboard')
 
# handler404 = 'servcenter.urls.handle_404'
