from pydantic import BaseModel

class FailedResponse(BaseModel):
    success: bool = False
    message: str

    def to_json(self):
        return {
            "success": str(self.success),
            "message": str(self.message)
        }


class SuccessResponse(BaseModel):
    success: bool = True
    message: str

    def to_json(self):
        return {
            "success": str(self.success),
            "message": str(self.message)
        }