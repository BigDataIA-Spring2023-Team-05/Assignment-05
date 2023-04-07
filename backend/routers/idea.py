from fastapi import APIRouter, status, Depends
from schemas.index import TokenData
from sqlalchemy.orm import Session
from config import db
from repository import user
from fastapi.security import OAuth2PasswordRequestForm
from middlewares.oauth2 import get_current_user
from utils.open_ai_chat import open_ai_obj

router = APIRouter(
    prefix='/idea',
    tags=['Idea']
)

get_db = db.get_db


@router.get('/get-user-segments-for-product-idea')
def get_all_user_based_on_idea(idea:str, get_current_user: TokenData = Depends(get_current_user)):
    result = open_ai_obj.generate_user_segment_for_product_idea(idea= idea)
    
    return {
        'success': True,
        'user_segments': result
    }


@router.get('/get-product-ideas-for-user-segment')
def get_all_product_ideas_for_user_segment(idea:str, get_current_user: TokenData = Depends(get_current_user)):
    result = open_ai_obj.generate_product_idea_for_user_segment(user_segment= idea)
    
    return {
        'success': True,
        'user_segments': result
    }


