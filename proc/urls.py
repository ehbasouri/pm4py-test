from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home/', views.main_view),
    path('uploadfilealpha/', views.upload_file_alpha),
    path('uploadfileinductive/', views.upload_file_inductive),
    path('uploadfileheuristics/', views.upload_file_heuristics),
    path('model/', views.model_view),
    path('confirm/', views.confirm_view),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
