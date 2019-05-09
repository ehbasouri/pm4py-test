from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.main_view),
    path('uploadfile/', views.upload_file),
    path('model/', views.model_view),
    path('confirm/', views.confirm_view),
]