from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls", namespace="users")),
    path('', include("web.urls", namespace="web")),
    path('posts/', include("posts.urls", namespace="posts")),

]

# if settings.DEBUG:
#     urlpatterns += (
#         static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + 
#         static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)  

#     )
