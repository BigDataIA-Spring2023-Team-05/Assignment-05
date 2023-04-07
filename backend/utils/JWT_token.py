from datetime import datetime, timedelta
from jose import JWTError, jwt
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from schemas.index import TokenData
from typing import List, Optional, Union

load_dotenv()



def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.environ.get('SECRET_KEY'), algorithm = os.environ.get('ALGORITHM'))
    return encoded_jwt

def verify_token(token:str, credentials_exception):
    try:
        payload = jwt.decode(token,  os.environ.get('SECRET_KEY'), algorithms=os.environ.get('ALGORITHM'))
        email: str = payload.get("email")

        
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(id = payload.get("id"), email=email)
        return token_data
    except (JWTError):
        raise credentials_exception
    
def verify_token_for_email(token:str):
    try:
        payload = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=os.environ.get('ALGORITHM'))
        email: str = payload.get("email")        
        idea_id: str = payload.get("idea_id")        

        token_data = {
            "email": email,
            "idea_id": idea_id,
            }
        return token_data
    except Exception as e:
        print(e)
        return None
    
def generate_email_token(email_id:str, idea_id:int) -> str:
    expire = datetime.utcnow() + timedelta(days=30)
    payload = {
        "email": email_id,
        "idea_id": idea_id,
        "exp": expire
    }

    encoded_jwt = jwt.encode(payload, os.environ.get('SECRET_KEY'), algorithm = os.environ.get('ALGORITHM'))
    return encoded_jwt
