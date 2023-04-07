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


    def send_html_email(self, email:str, token_link: str, html_code:str, feature_list:str, mission_statement: str):
        HTML_EMAIL_CONTENT = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Product Idea</title>
            </head>
            <body>
                <h1>Hey, I have brainstormed some ideas!</h1>
                <p>I think <em>product_idea</em> is a good fit for our team, check out details below:</p>
                <h2>Mission Statement:</h2>
                <p><em>{mission_statement}</em></p>
                <h2>Here are the few prototype features that might be available:</h2>
                <br/>
                {feature_list}
                <br/>
                <br/>
                <p>Prototype link: <a href="<HTML file>">HTML file</a></p>
                <p>Please give your feedback, I would love to hear back from you: <a href="{token_link}">{token_link}</a></p>
                <p>Thanks.</p>
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
