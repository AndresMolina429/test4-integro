from django.urls import path
from .views import Test4View

app_name = 'test4_app'

urlpatterns = [
    path('', Test4View.as_view(), name='test4') 
]