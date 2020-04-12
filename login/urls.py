from . import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', csrf_exempt(views.signup), name='signup'),
]