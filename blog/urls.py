from django.contrib import admin
from django.urls import path
from posts.views import home, post_list_view, post_detail_view, created_post
from users.views import register_view, login_veiw, logout_view
from django.conf.urls.static import static
from django.conf import settings


users_patterns = [
    path("register/", register_view, name="register"),
    path("login/", login_veiw, name="login"),
    path("logout/", logout_view, name="logout"),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", home),
    path("posts/", post_list_view),
    path("posts/<int:post_id>/", post_detail_view),
    path("posts/create", created_post)
] + users_patterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
