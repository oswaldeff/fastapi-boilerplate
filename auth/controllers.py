
from auth.models import User

def signup(request, body, db):
    phone = body.phone
    password = body.password

    signed_user = User(phone=phone, password=password)
    db.add(signed_user)
    db.commit()
    db.refresh(signed_user)

    return signed_user
