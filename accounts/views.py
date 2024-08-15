from rest_framework import viewsets
from .models import Accounts
from .serializers import AccountsSerializer
 
class AccountsViewSet(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer