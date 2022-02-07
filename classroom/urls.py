from django.urls import path

from .views import ClassRoomListView

urlpatterns = [
    path("", ClassRoomListView.as_view(), name="classroom_list"),
    path("classroom/create", ClassRoomListView.as_view(), name="classroom_create"),
]
