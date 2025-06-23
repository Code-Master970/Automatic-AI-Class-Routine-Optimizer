from django.urls import path
from . import views
from .views import schedule_view
urlpatterns = [
    #path('periods/', views.create_periods_view, name='view_periods'),
    path('schedule/', views.schedule_view, name='schedule_display'),
    path('create-periods/', views.create_periods_view, name='create_periods'),
]
