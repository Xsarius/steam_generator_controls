from django.urls import path
from webcontrol.views import Index

urlpatterns = [
    path('', Index.as_view())
]