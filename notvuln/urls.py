from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path
from core import views
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('', RedirectView.as_view(url='all')),
    path('all', views.post_list),
    path('submit', views.create_post)
]
