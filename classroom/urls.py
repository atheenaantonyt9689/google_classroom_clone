from django.urls import path

from .views import ClassRoomCreateView, ClassRoomListView

urlpatterns = [
    path("", ClassRoomListView.as_view(), name="book_list"),
    path("classroom/create", ClassRoomCreateView.as_view(), name="classroom_create"),
]
