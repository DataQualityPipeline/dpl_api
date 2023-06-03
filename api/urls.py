from django.urls import path
from api.views import UserView

urlpatterns = [
    path('', UserView.as_view()),
]