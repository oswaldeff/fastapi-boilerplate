
from fastapi import APIRouter
from fastapi import Depends, Request
from sqlalchemy.orm import Session

from settings.database import db_orm
from auth import controllers, schemas

APIs = APIRouter(prefix="/auth", tags=['계정'])

@APIs.post("/signup", response_model=schemas.Res_Post_Signup, summary="회원가입")
async def signup(request: Request, body: schemas.Body_Post_Signup, db: Session=Depends(db_orm.session)):
    return controllers.signup(request, body, db)
