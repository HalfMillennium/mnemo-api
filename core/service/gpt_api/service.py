import openai
import os
from dotenv import load_dotenv

DEFAULT_WORD_COUNT = 250

class GptService:
    def __init__(self):
        load_dotenv()
        self.OPEN_AI_KEY = os.getenv('OPEN_AI_KEY')
        openai.api_key = self.OPEN_AI_KEY
    
    def generate_diary_entry(self, stories, name_prompt, word_count = DEFAULT_WORD_COUNT) -> str:
        full_prompt = self.__build_full_diary_prompt(stories, name_prompt, word_count)
        response = self.get_response(full_prompt)
        return response
        
    def get_response(self, prompt):
        messages = []
        if prompt: 
            messages.append( 
                {"role": "user", "content": prompt}, 
            ) 
            chat = openai.ChatCompletion.create( 
                model="gpt-3.5-turbo", messages=messages 
            )
        return chat.choices[0].message.content

    def __build_full_diary_prompt(self, stories, name_prompt, word_count):
        stories_list = ', '.join(str(story) for story in stories)
        diary_prompt = (
            f"From the following set of JSON objects providing information "
            f"about recent news stories pertaining to {name_prompt}, "
            f"write a {word_count}-word diary entry, detailing their perspective "
            f"on the events, in a first-person perspective. Here are the stories: [{stories_list}]. "
            f"The diary entry should be funny and cynical. "
            f"Include links to relevant articles next to keywords, if possible. "
            f"The words in the links are not included in the {word_count}-word maximum."
        )
        return diary_prompt