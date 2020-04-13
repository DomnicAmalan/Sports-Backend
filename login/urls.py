from . import views
from django.urls import path

urlpatterns = [
    path('signup/?<str:Username>', views.UserViewset.as_view(), name='signup'),
]