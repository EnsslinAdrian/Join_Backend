from rest_framework import serializers
from ..models import Member, Task

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'
    
class MembersSerializer(serializers.ModelSerializer):
    task_count = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = '__all__'

    def get_task_count(self, obj):
        return obj.tasks.count()