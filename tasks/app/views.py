from rest_framework import generics
from .serializers import MembersSerializer, Member, TaskSerializer, Task
from rest_framework.permissions import AllowAny

class MembersView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MembersSerializer
    permission_classes = [AllowAny]

class MemberSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MembersSerializer
    permission_classes = [AllowAny]

class MemberTasksView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        url_member_id = self.kwargs.get('pk')
        return Task.objects.filter(member_id=url_member_id)
    
class MemberSingleTaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]




