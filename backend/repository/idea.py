from sqlalchemy.orm import Session
from models.index import IdeasModel
from schemas.index import SuccessResponse, FailedResponse
from fastapi import status
from fastapi.responses import JSONResponse


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