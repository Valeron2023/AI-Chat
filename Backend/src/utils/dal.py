from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from .app_config import AppConfig

BaseModel = declarative_base()


class Dal:

    def create_session(self):
        engine = create_engine(AppConfig.connection_string)
        BaseModel.metadata.create_all(engine)
        session_creator = sessionmaker(bind=engine)
        session = session_creator()
        return session


dal = Dal()
