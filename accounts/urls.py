from django.conf.urls import url
from .views import login, profile, sign_up, log_out


urlpatterns = [
    # The kwargs below are for self documentation & reverse URL resolution (e.g. menus).

    # Accounts
    url(r'^login/', login, name='login'),
    url(r'^profile/', profile, name='profile'),
    url(r'^sign_up/', sign_up, name='sign_up'),
    url(r'^log_out/', log_out, name='log_out'),
]