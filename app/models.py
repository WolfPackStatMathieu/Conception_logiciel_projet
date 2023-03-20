from .database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE


class Note(Base):
    __tablename__ = 'notes' #tells SQLAlchemy to use the provided string as the table name in the database.
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    category = Column(String, nullable=True)
    published = Column(Boolean, nullable=False, default=True)
    createdAt = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
    updatedAt = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())

