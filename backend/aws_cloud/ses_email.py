import boto3
import os
from dotenv import load_dotenv

load_dotenv()

class Email:
    def __init__(self) -> None:
        self.client = boto3.client(
            'ses',
            region_name='ap-southeast-1',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
            aws_secret_access_key=os.environ.get('AWS_ACCESS_KEY_SECRET')
        )

        self.CHARSET = "UTF-8"


    def send_html_email(self, email:str, token_link: str):
        HTML_EMAIL_CONTENT = f"""
            <html>
                <head></head>
                <h1 style='text-align:center'>Password reset</h1>
                <p>Need to reset your password?</p>
                </br>
                <p>Use your secret code!</p>
                </br></br></br>
                </br></br></br>
                <p>Enter the secret code above. It will expire in 5 minutes.</p>
                </br></br>
                <p>If you did not forget your password, you can ignore this email.</p>
                <a href="http://localhost:8501/register?user_token={token_link}">Click here</a>
                <br/><br/>
                copy paste this:
                http://localhost:8501/register?user_token={token_link}
                </body>
            </html>
        """


        response = self.client.send_email(
            Destination={
                "ToAddresses": [
                    f"{email}",
                ],
            },
            Message={
                "Body": {
                    "Html": {
                        "Charset": self.CHARSET,
                        "Data": HTML_EMAIL_CONTENT,
                    }
                },
                "Subject": {
                    "Charset": self.CHARSET,
                    "Data": "Team 5 Assignemnt 5",
                },
            },
            Source="jain.rishabh2@northeastern.edu",
        )

        print(response)

emailObj = Email()