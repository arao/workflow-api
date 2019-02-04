from django.conf.urls import url
from rest_framework import routers

from apps.auth.views import UserView, ResetPasswordView

router = routers.SimpleRouter()
router.register('user', UserView)

urlpatterns = router.urls

urlpatterns += [
    url('^user/reset-password/(?P<token>\w+-\w+--\d+)/$', ResetPasswordView.as_view(), name='reset-password')
]
