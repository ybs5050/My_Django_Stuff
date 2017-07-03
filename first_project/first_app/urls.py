from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^new/', views.index2, name='index2'),
]
