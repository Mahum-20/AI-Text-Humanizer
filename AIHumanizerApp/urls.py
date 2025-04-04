from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('humanize/', views.humanize_text_api, name='humanize_text'),
]