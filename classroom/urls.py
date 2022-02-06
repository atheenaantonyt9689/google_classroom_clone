from django.urls import path

from .views import ClassRoomListView

urlpatterns = [
    path("", ClassRoomListView.as_view(), name="book_list"),
]