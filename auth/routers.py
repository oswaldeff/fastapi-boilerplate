
from fastapi import APIRouter
from fastapi import Depends, Request
from sqlalchemy.orm import Session

from settings import database
from auth import controllers

APIs = APIRouter(prefix="/auth", tags=['계정'])

@APIs.get("/signup", response_model=None, summary="회원가입")
def signup(request: Request, body: None, db: Session=Depends(database.session)):
    return controllers.signup(request, body, db)
