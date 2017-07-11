from django.conf.urls import url
from .views import create, edit, delete, launch, my_robits


urlpatterns = [
    # The kwargs below are for self documentation & reverse URL resolution (e.g. menus).

    # Workspace
    url(r'^create/', create, name='create'),
    url(r'^edit/(?P<pk>\d+)', edit, name='edit'),
    url(r'^delete/', delete, name='delete'),
    url(r'^launch/', launch, name='launch'),
    url(r'^my_robits/', my_robits, name='my_robits'),

]