from rest_framework import serializers
from chat_room.models import ChatGroup, GroupMessage

class ChatGropuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatGroup
        fields = ['id', 'group_name']

class GroupMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMessage
        fields = ['id', 'group', 'author', 'body', 'created']
        read_only_fields = ['author', 'created']
        
