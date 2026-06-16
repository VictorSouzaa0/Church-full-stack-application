from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .models import Archdiocese, Church, People, Role
from .serliazers import ArchdioceseSerializers, ChurchSerializers, PeopleSerializers, RoleSerializers


class ArchdioceseCreateView(CreateAPIView):
    queryset = Archdiocese.objects.all()
    serializer_class = ArchdioceseSerializers
    permission_classes = [IsAdminUser, IsAuthenticated]

class ArchdioceseListView(ListAPIView):
    queryset = Archdiocese.objects.all()
    serializer_class = ArchdioceseSerializers
    permission_classes = [AllowAny]

class ArchdioceseDestroy(DestroyAPIView):
    serializer_class = ArchdioceseSerializers
    def get_queryset(self):
        archdiocese_id = self.kwargs['pk']
        return Archdiocese.objects.filter(id=archdiocese_id)
    permission_classes = [IsAdminUser, IsAuthenticated]   

class ArchdioceseListViewById(ListAPIView):
    serializer_class = ArchdioceseSerializers
    def get_queryset(self):
        archdiocese_id = self.kwargs['archdiocese_id']
        return Archdiocese.objects.filter(id=archdiocese_id)
    permission_classes = [AllowAny]


class ChurchCreateView(CreateAPIView):
    queryset = Church.objects.all()
    serializer_class = ChurchSerializers
    permission_classes = [IsAdminUser, IsAuthenticated]


class ChurchListView(ListAPIView):
    queryset = Church.objects.all()
    serializer_class = ChurchSerializers
    permission_classes = [AllowAny]

class ChurchDestroyView(DestroyAPIView):
    serializer_class = ChurchSerializers
    def get_queryset(self):
        church_id = self.kwargs['pk']
        return Church.objects.filter(id=church_id)
    permission_classes = [IsAdminUser,IsAuthenticated]

class ChurchListViewById(ListAPIView):
    serializer_class = ChurchSerializers
    def get_queryset(self):
        church_id = self.kwargs['church_id']
        return Church.objects.filter(id=church_id)
    permission_classes = [AllowAny]

class PeopleCreateView(CreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializers
    permission_classes = [IsAdminUser, IsAuthenticated]

class PeopleListView(ListAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializers
    permission_classes = [AllowAny]

class PeopleDestroyView(DestroyAPIView):
    serializer_class = People
    def get_queryset(self):
        people_id = self.kwargs['pk']
        return People.objects.filter(id=people_id)
    permission_classes = [IsAdminUser, IsAuthenticated]

class PeopleListViewById(ListAPIView):
    serializer_class = PeopleSerializers
    def get_queryset(self):
        people_id = self.kwargs['people_id']
        return People.objects.filter(id=people_id)
    permission_classes = [AllowAny]



class RoleCreateView(CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializers
    permission_classes = [IsAdminUser, IsAuthenticated]

class RoleListView(ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializers
    permission_classes = [AllowAny]

class RoleDestroyAPiView(DestroyAPIView):
    serializer_class = RoleSerializers
    def get_queryset(self):
        role_id = self.kwargs['pk']
        return Role.objects.filter(id=role_id)
    permission_classes = [IsAdminUser, IsAuthenticated]

class RoleListViewById(ListAPIView):
    serializer_class = RoleSerializers
    def get_queryset(self):
        role_id = self.kwargs['role_id']
        return Role.objects.filter(id=role_id)
    permission_classes = [AllowAny]