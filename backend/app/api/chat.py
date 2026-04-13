from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ai_engine import generate_ai_reply

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/", response_model=ChatResponse)
def chat_message(request: ChatRequest):
    reply = generate_ai_reply(request.message)
    return ChatResponse(reply=reply)
