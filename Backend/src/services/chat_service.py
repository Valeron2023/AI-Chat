import uuid
from fastapi import HTTPException, status
from openai import OpenAI
from models.chat_model import ConversationModel, MessageModel, MessageRequestSchema
from utils.dal import dal
from utils.app_config import AppConfig


class ChatService:

    def __init__(self) -> None:
        self.session = dal.create_session()
        self.client = OpenAI(api_key=AppConfig.openai_api_key)

    def send_message(self, request: MessageRequestSchema) -> dict:
        conversation_id = request.conversation_id

        if not conversation_id:
            conversation_id = str(uuid.uuid4())
            conversation = ConversationModel(id=conversation_id)
            self.session.add(conversation)
            self.session.commit()

        user_message = MessageModel(
            id=str(uuid.uuid4()),
            conversation_id=conversation_id,
            role="user",
            content=request.message,
        )
        self.session.add(user_message)
        self.session.commit()

        history = (
            self.session.query(MessageModel)
            .filter(MessageModel.conversation_id == conversation_id)
            .order_by(MessageModel.created_at)
            .all()
        )
        openai_messages = [{"role": m.role, "content": m.content} for m in history]

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=openai_messages,
            )
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(e))

        assistant_reply = response.choices[0].message.content

        assistant_message = MessageModel(
            id=str(uuid.uuid4()),
            conversation_id=conversation_id,
            role="assistant",
            content=assistant_reply,
        )
        self.session.add(assistant_message)
        self.session.commit()

        return {"conversation_id": conversation_id, "reply": assistant_reply}

    def close(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
