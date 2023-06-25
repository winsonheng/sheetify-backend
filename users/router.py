from users.viewsets import UserViewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', UserViewsets)
