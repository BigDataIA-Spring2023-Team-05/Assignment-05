from sqlalchemy.orm import Session
from models.index import IdeasModel, EmailRatingModel
from schemas.index import SuccessResponse, FailedResponse
from fastapi import status
from fastapi.responses import JSONResponse
from aws_cloud.ses_email import emailObj
from utils.JWT_token import generate_email_token
from sqlalchemy import and_

def create(user_id:int, title: str, features:str, db: Session):
    try:
        new_idea = IdeasModel(user_id= user_id, idea_title = title, features= features)
        db.add(new_idea)
        db.commit()
        db.refresh(new_idea)
        return SuccessResponse(message= f"User's idea stored successfully!")
    except Exception as e:
        print(e)
        return JSONResponse(
                status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
                content= FailedResponse(message= f"Internal server exception {str(e.with_traceback)}")
            )
    
def get_all_ideas(user_id:int, db: Session):
    ideas = db.query(IdeasModel).filter(IdeasModel.user_id == user_id).all()
    return ideas

def send_email(email: str, idea_id:int, db: Session):
    try:
        idea = db.query(EmailRatingModel).filter(and_(EmailRatingModel.email == email, EmailRatingModel.idea_id == idea_id)).first()

        if idea:
            return JSONResponse(
                status_code= status.HTTP_409_CONFLICT,
                content= FailedResponse(message= f"email is already sent!").to_json()
            )


        new_email = EmailRatingModel(idea_id= idea_id, email = email)
        db.add(new_email)
        db.commit()
        db.refresh(new_email)

        token_link = generate_email_token(email_id= email, idea_id= idea_id)
        
        emailObj.send_html_email(email= email, token_link=token_link)

        return SuccessResponse(message= f"User's email sent successfully!")
    
    except Exception as e:
        print(e)
        return JSONResponse(
                status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
                content= FailedResponse(message= f"Internal server exception {str(e.with_traceback)}")
            )