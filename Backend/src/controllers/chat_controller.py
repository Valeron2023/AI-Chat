from fastapi import APIRouter, status
from models.chat_model import MessageRequestSchema, MessageResponseSchema
from services.chat_service import ChatService

router = APIRouter()


@router.post("/api/chat/send", response_model=MessageResponseSchema, status_code=status.HTTP_200_OK)
def send_message(request: MessageRequestSchema):
    with ChatService() as chat_service:
        result = chat_service.send_message(request)
        return result
