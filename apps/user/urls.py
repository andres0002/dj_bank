# django
from django.urls import path, include
# third
# own
from apps.user.views import Logout

urlpatterns = [
    path('admin_bank/', include(('apps.user.urls_admin', 'admin'))),
    path('client/', include(('apps.user.urls_client', 'client'))),
    path('logout/', Logout.as_view(), name='logout'),
]