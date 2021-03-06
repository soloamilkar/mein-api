from django.urls import path
from .views import MainUserChangePassword, MainUserLogin, MainUserView, WaiterView
urlpatterns = [
    path('', MainUserView.as_view(), name="owners-create"),
    path('google/', MainUserView.as_view(), name="owners-create-google"),
    path('meseros/', WaiterView.as_view(), name="meseros-create"),
    path('login/', MainUserLogin.as_view(), name="login"),
    path('change-pass/<str:user_uuid>/',
         MainUserChangePassword.as_view(), name="change-password"),
]
