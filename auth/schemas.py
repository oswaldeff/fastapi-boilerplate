
from typing import List, Optional

from pydantic import BaseModel

# signup
class Res_Post_Signup(BaseModel):
    status: str
    user_data: object

class Body_Post_Signup(BaseModel):
    phone: str
    password: Optional[str]
