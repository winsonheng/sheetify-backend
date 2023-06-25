from rest_framework import viewsets
from users.serializers import UserSerializers
from users.models import User
 
 
class UserViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers