from django.contrib import admin
from django.urls import path
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('report/', views.ReportView.as_view(), name='report'),
    path('graph/<report_id>/', views.graph, name='graph'),
]
