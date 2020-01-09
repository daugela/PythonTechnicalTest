import re
from bonds.models import Bonds
from .serializers import BondSerializer
from rest_framework import viewsets, permissions
from rest_framework.authentication import BasicAuthentication

from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import Profile


class HelloWorld(APIView):

    @staticmethod
    def get(self):
        return Response("Hello World!")


class BondViewSet(viewsets.ModelViewSet):

    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = BondSerializer

    def get_queryset(self):
        optional_legal_name = self.request.query_params.get("legal_name")
        if optional_legal_name is not None:
            if re.match(r"^\w+$", optional_legal_name):
                return Bonds.objects.filter(owner=self.request.user.profile, legal_name=optional_legal_name)
            else:
                return {}
        return Bonds.objects.filter(owner=self.request.user.profile)

    def perform_create(self, serializer):
        owner_profile = Profile.objects.get(user=self.request.user)
        serializer.save(owner=owner_profile)
