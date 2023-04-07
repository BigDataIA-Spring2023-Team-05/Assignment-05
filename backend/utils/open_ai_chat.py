# %%
import openai
from dotenv import load_dotenv
import os

load_dotenv()

# %%
class OpenAIChat:
    def __init__(self) -> None:
        openai.api_key = os.environ.get('OPEN_AI_API_KEY')

    def generate_user_segment_for_product_idea(self, idea: str) -> str:
        completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages = [
                    {'role':'system', 'content': 'you are an assistant who generates upto 10 numbered list of user segments without description or any other extra information for a given product idea'},
                    {'role': 'user', 'content': f'create a list of user segments for product idea \'{idea}\'?'}
                ],
                temperature = 0.70,
                
            )
        
        result = completion.choices[0].message.content
        splitted_result = result.split('\n\n')

        if len(splitted_result) > 1:
            return splitted_result[1]
        else:
            return splitted_result[0]

    
    def generate_product_idea_for_user_segment(self, user_segment: str) -> str:
        completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages = [
                    {'role': 'user', 'content': f'create upto 10 numbered list of product ideas without description for user segment \'{user_segment}\'?'}
                ],
                temperature = 0.70,
            )

        result = completion.choices[0].message.content
        splitted_result = result.split('\n\n')

        if len(splitted_result) > 1:
            return splitted_result[1]
        else:
            return splitted_result[0]
        
    def generate_feature_list_for_product_idea(self, product_idea: str) -> str:
        completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages = [
                    {'role': 'user', 'content': f'create numbered upto 10 feature list for the product idea \'{product_idea}\' with every list item in next line'}
                ],
                temperature = 0.70,
            )



        result = completion.choices[0].message.content
        print(result)

        splitted_result = result.split('\n\n')

        print(splitted_result)
        if len(splitted_result) > 1:
            return splitted_result[1]
        else:
            return splitted_result[0]
        

    def generate_to_do_list_for_product_feature(self, product_feature: str) -> str:
        completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages = [
                    {'role': 'user', 'content': f'create upto 10 numbered to-do list for product feature \'{product_feature}\'?'}
                ],
                temperature = 0.70,
            )



        result = completion.choices[0].message.content
        print(result)

        splitted_result = result.split('\n\n')

        print(splitted_result)
        if len(splitted_result) > 1:
            return splitted_result[1]
        else:
            return splitted_result[0]
        

    def generate_to_do_list_for_product_feature(self, product_feature: str) -> str:
        completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages = [
                    {'role': 'user', 'content': f'create a numbered to-do list for product feature \'{product_feature}\'?'}
                ],
                temperature = 0.70,
            )



        result = completion.choices[0].message.content
        print(result)

        splitted_result = result.split('\n\n')

        print(splitted_result)
        if len(splitted_result) > 1:
            return splitted_result[1]
        else:
            return splitted_result[0]

# %%
open_ai_obj = OpenAIChat()
# openaiobj.generate_user_segment_for_product_idea('sql query generator')


# %%
# print(openaiobj.generate_product_idea_for_user_segment('data engineers'))


# %%
