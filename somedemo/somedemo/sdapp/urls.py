from django.urls import path
from . import views
urlpatterns = [
    path('paginator/',views.testPaginator)
]