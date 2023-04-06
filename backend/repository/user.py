from sqlalchemy.orm import Session
from models.index import UserModel
from schemas.index import LoginResponse, User, SuccessResponse, FailedResponse
from utils import hashing, JWT_token
from fastapi import status
from fastapi.responses import JSONResponse


def create(request: User, db: Session):
    try:
        user = db.query(UserModel).filter(UserModel.email == request.email).first()

        if user:
            return JSONResponse(
                status_code= status.HTTP_409_CONFLICT,
                content= FailedResponse(message= f"User with the email '{request.email}' already exists!")
            )

        new_user = UserModel(username=request.username, email=request.email, password= hashing.Hash().get_hashed_password(request.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return SuccessResponse(message= f"User with {request.email} registered successfully!")
    
    except Exception as e:
        print(e)
        return JSONResponse(
                status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
                content= FailedResponse(message= f"Internal server exception {str(e.with_traceback)}")
            )
    

def find_user(email: str, password: str, db: Session):
    user = db.query(UserModel).filter(UserModel.email == email).first()
    
    if not user:
        return JSONResponse(
                status_code= status.HTTP_404_NOT_FOUND,
                content= FailedResponse(message= f"User with the email '{email}' not found").to_json()
            )
    
    if not hashing.Hash().verify_password(user.password, password=password):
        return JSONResponse(
                status_code= status.HTTP_401_UNAUTHORIZED,
                content= FailedResponse(message= "invalid credentials").to_json()
            )
    
    access_token = JWT_token.create_access_token(data={"id": user.id, "email": user.email})
    
    return LoginResponse(username= str(user.username), email= str(user.email), access_token= access_token, token_type= 'bearer')
