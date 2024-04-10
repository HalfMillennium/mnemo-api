import openai
import os
from mnemo_api.mnemo_logic.search.utils.search_tools.search_resource_service import SearchResourceService
from dotenv import load_dotenv

DEFAULT_DIARY_ENTRY_WORD_COUNT = 250
DEFAULT_SUMMARY_WORD_COUNT = 100

class GptService:
    def __init__(self):
        load_dotenv()
        self.OPEN_AI_KEY = os.getenv('OPEN_AI_KEY')
        openai.api_key = self.OPEN_AI_KEY
    
    async def generate_diary_entry(self, stories, entity_name, word_count = DEFAULT_DIARY_ENTRY_WORD_COUNT) -> str:
        full_prompt = self.__build_full_diary_prompt(stories, entity_name, word_count)
        response = self.get_response(full_prompt)
        return response

    async def generate_summary(self, entity_name, word_count = DEFAULT_SUMMARY_WORD_COUNT) -> str:
        wiki_service = SearchResourceService('Wiki')
        summary = await wiki_service.execute_query(search_term=entity_name)
        full_prompt = self.__build_full_summary_prompt(entity_name, summary, word_count)[:2000]
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
            f"generate a {word_count}-word summary about them: {wiki_content}"
        )
        return summary_prompt

    def __build_full_diary_prompt(self, stories, entity_name, word_count):
        stories_list = ', '.join(str(story) for story in stories)
        diary_prompt = (
            f"From the following set of JSON objects providing information "
            f"about recent news stories pertaining to {entity_name}, "
            f"write a {word_count}-word diary entry, detailing their perspective "
            f"on the events, in a first-person perspective. Here are the stories: [{stories_list}]. "
            f"The diary entry should have a very humorous and slightly cynical tone. It should be in first-person perspective from the point of view of the entity '{entity_name}'."
            f"and reflect the entity's personality and emotions.  The tone should be conversational and relatable. "
            f"Include links to relevant articles next to keywords, if possible. "
            f"The words in the links are not included in the {word_count}-word maximum."
        )
        return diary_prompt