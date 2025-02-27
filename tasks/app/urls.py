from django.urls import path
from .views import MembersView, MemberSingleView, MemberTasksView, MemberSingleTaskView

urlpatterns = [
    path('members/', MembersView.as_view()),
    path('members/<int:pk>/', MemberSingleView.as_view(), name='members-detail'),
    path('members/<int:pk>/tasks/', MemberTasksView.as_view(), name='members-tasks'),
    path('tasks/<int:pk>/', MemberSingleTaskView.as_view(), name='task-detail'),
]