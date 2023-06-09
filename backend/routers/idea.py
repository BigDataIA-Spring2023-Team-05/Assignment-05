from fastapi import APIRouter, status, Depends, Request, Header
from schemas.index import TokenData, MVPIdea, EmailRate
from sqlalchemy.orm import Session
from config import db
from repository import idea
from fastapi.security import OAuth2PasswordRequestForm
from middlewares.oauth2 import get_current_user
from utils.open_ai_chat import open_ai_obj
import json
from fastapi.responses import JSONResponse
from typing import List
from typing import Union
from typing_extensions import Annotated

router = APIRouter(
    prefix='/idea',
    tags=['Idea']
)

get_db = db.get_db


@router.get('/get-user-segments-for-product-idea')
def get_all_user_based_on_idea(idea:str, get_current_user: TokenData = Depends(get_current_user)):
    result = open_ai_obj.generate_user_segment_for_product_idea(idea= idea)
    
    if result != None:
        my_list = result.strip().split("\n")
    
    return {
        'success': True,
        'user_segments': my_list
    }


@router.get('/get-product-ideas-for-user-segment')
def get_all_product_ideas_for_user_segment(idea:str, get_current_user: TokenData = Depends(get_current_user)):
    result = open_ai_obj.generate_product_idea_for_user_segment(user_segment= idea)
    

    if result != None:
        my_list = result.strip().split("\n")

    return {
        'success': True,
        'product_ideas': my_list
    }



@router.get('/get-features-list-for-product-ideas')
def get_feature_list_for_product_idea(product_idea:str, get_current_user: TokenData = Depends(get_current_user)):
    result = open_ai_obj.generate_feature_list_for_product_idea(product_idea= product_idea)
    
    if result != None:
        my_list = result.strip().split("\n")

    return {
        'success': True,
        'features_list': my_list
    }



@router.get('/get-to-do-list-for-product-feature')
def get_to_do_list_for_product_feature(product_feature:str, get_current_user: TokenData = Depends(get_current_user)):
    result = open_ai_obj.generate_to_do_list_for_product_feature(product_feature = product_feature)
    
    if result != None:
        my_list = result.strip().split("\n")

    return {
        'success': True,
        'features_list': my_list
    }


@router.post('/approve-mvp')
def approve_mvp_idea(request: MVPIdea, get_current_user: TokenData = Depends(get_current_user), db: Session = Depends(get_db)):
    return idea.create(user_id= get_current_user.id, title = request.idea_title, features = request.features, db=db)



@router.post('/get-all-user-ideas', status_code= status.HTTP_200_OK, response_model= List[MVPIdea])
def get_all_ideas(get_current_user: TokenData = Depends(get_current_user), db: Session = Depends(get_db)):
    ideas = idea.get_all_ideas(user_id= get_current_user.id, db=db)
    
    if len(ideas) == 0:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                'success': False, 
                "message": "user do not have any idea"
            }
        )

    return ideas
         

@router.post('/send-email-for-feedback')
def send_email_feedback(mission_statement:str, html_code:str, email_id:str, idea_title: str, get_current_user: TokenData = Depends(get_current_user), db: Session = Depends(get_db)):    
    return idea.send_email(mission_statement=mission_statement, html_code=html_code, email= email_id, idea_title= idea_title, user_id= get_current_user.id, db= db)


@router.post('/recieve-feedback-from-email')
def receive_feedback_from_email(request: EmailRate, review_token: Annotated[Union[str, None], Header()] = None, db: Session = Depends(get_db)):    
    return idea.add_feedback(token= review_token, rating= request.rating, feedback= request.feedback, db= db)



@router.get('/get-insights-of-idea')
def receive_summarized_feedback(idea_title: str, get_current_user: TokenData = Depends(get_current_user), db: Session = Depends(get_db)):    
    return idea.summarized_feedback(user_id=get_current_user.id, idea_title= idea_title, db= db)
