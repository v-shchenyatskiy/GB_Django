from django.urls import path

from users.views import login, RegistrationCreateView, profile, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),

    path('registration/', RegistrationCreateView.as_view(), name='registration'),
    # path('registration/', registration, name='registration'),

    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]
