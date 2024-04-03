import openai
import os
from search.utils.search_tools.search_resource_service import SearchResourceService
from dotenv import load_dotenv

DEFAULT_DIARY_ENTRY_WORD_COUNT = 250
DEFAULT_SUMMARY_WORD_COUNT = 100

class GptService:
    def __init__(self):
        load_dotenv()
        self.OPEN_AI_KEY = os.getenv('OPEN_AI_KEY')
        openai.api_key = self.OPEN_AI_KEY
    
    async def generate_diary_entry(self, stories, name_prompt, word_count = DEFAULT_DIARY_ENTRY_WORD_COUNT) -> str:
        full_prompt = self.__build_full_diary_prompt(stories, name_prompt, word_count)
        response = self.get_response(full_prompt)
        return response

    async def generate_summary(self, entity_name, word_count = DEFAULT_SUMMARY_WORD_COUNT) -> str:
        full_prompt = self.__build_full_summary_prompt(entity_name, word_count)
        wiki_service = SearchResourceService('Wiki')
        summary = await wiki_service.execute_query()
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

    def __build_full_summary_prompt(self, entity_name, wiki_content, word_count):
        summary_prompt = (
            f"Given the following Wikipedia information about {entity_name}, "
            f"generate a {word_count}-word summary about them."
        )
        return summary_prompt

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