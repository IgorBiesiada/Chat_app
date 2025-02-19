from django.urls import path
from chat_room.views import ChatGroupListCreateView, GroupMessageCreateView

app_name = 'chat_room'

urlpatterns = [
    path('add_chat/', ChatGroupListCreateView.as_view(), name='add_chat'),
    path('messages', GroupMessageCreateView.as_view(), name='messages')
]