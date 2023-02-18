
from sqlalchemy import Column, Integer, String
from settings.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    phone = Column(String)
    password = Column(String, nullable=True)
    naver_id = Column(String, nullable=True)
    kakao_id = Column(String, nullable=True)
    apple_id = Column(String, nullable=True)
    updated_at = Column(String)
    created_at = Column(String)
