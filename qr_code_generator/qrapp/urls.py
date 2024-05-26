from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from qrapp import views
from qrapp.views import UserCreateView

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    # path('history/', views.history, name='history'),
    # # path('register/', views.register, name='register'),
    # # path('login/', views.user_login, name='login'),
    # path("sign-up/", UserCreateView.as_view(), name="sign-up"),
    # path("accounts/", include("django.contrib.auth.urls")),
    # path("qrcode/", include("qrapp.urls")),
    # path('logout/', views.user_logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
app_name = 'qrapp'
