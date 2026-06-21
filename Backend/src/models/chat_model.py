import uuid
from typing import Optional
from sqlalchemy import Column, String, Text, Enum, ForeignKey, DateTime
from sqlalchemy.sql import func
from pydantic import BaseModel as BaseSchema
from utils.dal import BaseModel


class ConversationModel(BaseModel):
    __tablename__ = "conversations"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, server_default=func.now())


class MessageModel(BaseModel):
    __tablename__ = "messages"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    conversation_id = Column(String(36), ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False)
    role = Column(Enum("user", "assistant"), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())


class MessageRequestSchema(BaseSchema):
    conversation_id: Optional[str] = None
    message: str


class MessageResponseSchema(BaseSchema):
    conversation_id: str
    reply: str
