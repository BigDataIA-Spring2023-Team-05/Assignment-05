from sqlalchemy.orm import Session
from models.index import IdeasModel, EmailRatingModel
from schemas.index import SuccessResponse, FailedResponse
from fastapi import status
from fastapi.responses import JSONResponse
from aws_cloud.ses_email import emailObj
from utils.JWT_token import generate_email_token, verify_token_for_email
from sqlalchemy import and_

def create(user_id:int, title: str, features:str, db: Session):
    try:
        idea = db.query(IdeasModel).filter(and_(IdeasModel.idea_title == title, IdeasModel.user_id == user_id)).first()

        if idea:
            return JSONResponse(
                status_code= status.HTTP_409_CONFLICT,
                content= FailedResponse(message= f"Idea with this name already exists in your list!").to_json()
            )


        new_idea = IdeasModel(user_id= user_id, idea_title = title, features= features)
        db.add(new_idea)
        db.commit()
        db.refresh(new_idea)
        return SuccessResponse(message= f"User's idea stored successfully!")
    except Exception as e:
        print(e)
        return JSONResponse(
                status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
                content= FailedResponse(message= f"Internal server exception {str(e.with_traceback)}").to_json()
            )
    
def get_all_ideas(user_id:int, db: Session):
    ideas = db.query(IdeasModel).filter(IdeasModel.user_id == user_id).all()
    return ideas

def send_email(email: str, idea_title:str, user_id:int, db: Session):
    try:
        idea_val = db.query(IdeasModel).filter(and_(IdeasModel.idea_title == idea_title, IdeasModel.user_id == user_id)).first()
        
        idea_id = idea_val.id
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
                content= FailedResponse(message= f"Internal server exception {str(e.with_traceback)}").to_json()
            )
    
def add_feedback(token, rating: int, feedback: str, db: Session):
    print(token)
    if not (rating >= 1 and rating <= 5):
        return JSONResponse(
                status_code= status.HTTP_400_BAD_REQUEST,
                content= FailedResponse(message= "Please pass rating between 1-5").to_json()
            )
    

    try:
        tokenData = verify_token_for_email(token)
        print(tokenData)
        
        if tokenData is None:
            return JSONResponse(
            status_code= status.HTTP_401_UNAUTHORIZED,
            content= FailedResponse(message= "Unauthorized user").to_json()
        )

        emailRate = db.query(EmailRatingModel).filter(and_(EmailRatingModel.email == tokenData["email"], EmailRatingModel.idea_id == tokenData["idea_id"])).first()

        if not emailRate:
            return JSONResponse(
                status_code= status.HTTP_404_NOT_FOUND,
                content= FailedResponse(message= f"User rating not exists").to_json()
            )
        
        if emailRate.rating != None:
            return JSONResponse(
                status_code= status.HTTP_409_CONFLICT,
                content= FailedResponse(message= f"User rating already exists").to_json()
            )

        print(rating, feedback)
        
        emailRate.rating = rating
        emailRate.feedback = feedback

        db.add(emailRate)
        db.commit()
        db.refresh(emailRate)

        return JSONResponse(
            status_code= status.HTTP_200_OK,
            content= SuccessResponse(message= f"User rating added").to_json()
        )
            
    except Exception as e:
        print(e)
        return JSONResponse(
                status_code= status.HTTP_401_UNAUTHORIZED,
                content= FailedResponse(message= f"Unauthorized user with {e.with_traceback}").to_json()
            )