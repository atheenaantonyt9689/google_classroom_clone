from django.urls import path

from .views import ClassRoomCreateView, ClassRoomListView, ClassRoomEditView

urlpatterns = [
    path("", ClassRoomListView.as_view(), name="classroom_list"),
    path("classroom/create", ClassRoomCreateView.as_view(), name="classroom_create"),
    path("classroom/<int:pk>/edit", ClassRoomEditView.as_view(), name="classroom_edit"),
]
