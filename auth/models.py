
from pydantic import BaseModel

class User(BaseModel):
    id: str
    phone: str = "01000000000"
    naver_id: str | None = None
    kakao_id: str | None = None
    apple_id: str | None = None
    updated_at: str = "0000-00-00 00:00:00"
    created_at: str = "0000-00-00 00:00:00"
