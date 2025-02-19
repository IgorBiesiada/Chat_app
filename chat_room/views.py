from rest_framework.response import Response
from rest_framework import generics
from chat_room.models import ChatGroup, GroupMessage
from chat_room.serializer import ChatGropuSerializer, GroupMessageSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Create your views here.

class ChatGroupListCreateView(generics.ListCreateAPIView):
    queryset = ChatGroup.objects.all()
    serializer_class = ChatGropuSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)

class GroupMessageCreateView(generics.CreateAPIView):
    queryset = GroupMessage.objects.all()
    serializer_class = GroupMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)
        