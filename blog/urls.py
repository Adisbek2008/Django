from django.contrib import admin
from django.urls import path
from posts.views import home, post_list_view, post_detail_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", home),
    path("posts/", post_list_view),
    path("posts/<int:post_id>/", post_detail_view)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
