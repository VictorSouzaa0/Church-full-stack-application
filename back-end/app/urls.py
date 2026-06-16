from django.urls import path
from .views import *
from .views import PeopleListViewById
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Church API",
        default_version="1.0",
        description="API test",
        terms_of_service="http://github.com/VictorSouzaa0",
        contact=openapi.Contact(email="opa"),
        license=openapi.License(name="isso ae")
    ),
    public=True,
)

urlpatterns = [
    path('swagger/',schema_view.with_ui('swagger', cache_timeout=0)),
    path("people/",PeopleListView.as_view(), name='list-peoples'),
    path("people/",PeopleCreateView.as_view(), name='create-people'),
    path("people/<int:people_id>/",PeopleListViewById.as_view(),name='list-people-by-id' ),
    path('create-people/', PeopleCreateView.as_view(), name='Create-People'),
    path('people/<int:pk>/',PeopleDestroyView.as_view(), name='delete-user'),
    path('create-chuch/',ChurchCreateView.as_view(),name='craete-church'), 
    path('church/', ChurchListView.as_view(), name='list-church'),
    path('church/<int:pk>/', ChurchDestroyView.as_view(), name='delete-church'),
    path('church/<int:church_id>', ChurchListViewById.as_view(), name='list-church-by-id'),
    path('archdiocese/', ArchdioceseListView.as_view(),name='list-archdiocese'),
    path('archdiocese/<int:pk>/', ArchdioceseDestroy.as_view(), name='delete-archdiocese'),
    path('create-archdiocese/',ArchdioceseCreateView.as_view(),name='create-archdiocese'),
    path('archdiocese/<int:archdiocese_id>/', ArchdioceseListViewById.as_view(),name='list-archdiocese-by-id'),
    path('role/',RoleListView.as_view(), name='list-all-roles'),
    path('create-role/', RoleCreateView.as_view(), name='create-role'),
    path('role/<int:role_id>', RoleListViewById.as_view(), name='list-by-id'),
    path('role/<int:pk>', RoleDestroyAPiView.as_view(), name='delete-roles')

]