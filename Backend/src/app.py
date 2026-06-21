from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.chat_controller import router as chat_router
from middleware.exception_handler import register_exception_handlers
from uvicorn import run

server = FastAPI()

register_exception_handlers(server)

server.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

server.include_router(chat_router)

if __name__ == "__main__":
    run("app:server", port=4000, reload=True)
