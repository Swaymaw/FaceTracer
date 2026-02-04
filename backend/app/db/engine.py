from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base

from app.core.logger import logger
from app.core.config import settings
from sqlalchemy_utils import database_exists, create_database


class Engine:
    instance = None

    def __init__(self):
        self.check_database()
        self.engine = create_engine(settings.database_url, isolation_level="AUTOCOMMIT")
        self.local_session = sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False
        )
        self.check_tables()

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def check_database(self):
        logger.info("---Create DataBase---")
        if not database_exists(settings.database_url):
            create_database(settings.database_url)

    def check_tables(self):
        logger.info("---Create Tables---")
        Base.metadata.create_all(bind=self.engine)

    def register_face(self, user_id, face_embeddinng):
        pass

    def register_user(self, user_id, email):
        pass
