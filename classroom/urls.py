from django.urls import path

from .views import (
    AssignmentCreateView,    
    ClassRoomCreateView,
    ClassRoomListView,
    ClassRoomEditView,
    ClassroomDeleteView,
    ClassrooomDetailview,
)

urlpatterns = [
    path("", ClassRoomListView.as_view(), name="classroom_list"),
    path("classroom/create", ClassRoomCreateView.as_view(), name="classroom_create"),
    path("classroom/<int:pk>/edit", ClassRoomEditView.as_view(), name="classroom_edit"),
    path("classroom/<int:pk>/delete",ClassroomDeleteView.as_view(),name="classroom_delete"),
    path("classroom/<int:pk>/details",ClassrooomDetailview.as_view(),name="classroom_detailview"),
    # assignment_part
    path("assignment/create",AssignmentCreateView.as_view(),name="classroom_assignment_create"),
]
