from sqlalchemy import Column, DateTime, Integer, func

from config.database import Base


class BaseTable(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    updated_on = Column(DateTime(timezone=True), onupdate=func.now())
