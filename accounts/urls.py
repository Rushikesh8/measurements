from django.urls import path
from accounts.views import SignInView,GetTokenView
app_name="accounts"
urlpatterns = [
    path('sign-in/',SignInView.as_view(),name="sign-in"),
    path('get-token/',GetTokenView.as_view(),name="get-token")
]
