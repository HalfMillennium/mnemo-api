'''
'grequests' performs necessary monkey-patching operations on server start-up, and should be the first module imported
'''
from search.utils.search_tools.search_resource_service import SearchResourceService
from search.page_parser.page_parser_service import PageParserService
from gpt_api.service import GptService

class MnemoService:
    '''
    Return AI generated first-person POV diary entry based on the current events related to the search term name_prompt
    '''
    def fetch_diary_entry(entity_name):
        # TODO: Replace individual resource name and time_frame_days arguments to single 'ResourceSpec' object 
        # that includes optional field 'time_frame_days' and required field 'resource_name'
        google_news_search = SearchResourceService("Google News")
        page_html = google_news_search.execute_query(entity_name)
        google_news_page_parser = PageParserService("Google News", page_html)
        parsed_stories = list(google_news_page_parser.get_stories())
        if(parsed_stories == []):
            return f'Couldn\'t any stories related to "{entity_name}".'
        gpt_service = GptService()
        diary_entry_response = gpt_service.generate_diary_entry(parsed_stories, entity_name)
        return diary_entry_response

    '''
    Returns a set of relevant images related to the search term name_prompt
    '''
    def fetch_entity_images(entity_name):
        yahoo_images_search = SearchResourceService("Yahoo Images")
        images_list = list(yahoo_images_search.fetch_and_parse_images(name_prompt=entity_name))
        return images_list
    
    '''
    Returns a summary of the search term entity_name
    '''
    def fetch_entity_summary(entity_name):
        gpt_service = GptService()
        summary_response = gpt_service.generate_summary(entity_name)
        return summary_response

    def __print_google_news_stories(html_content):
        google_news_page_parser = PageParserService("Google News", html_content)
        articles = google_news_page_parser.get_stories() # { title: string, source: string, date_posted: string }[]
        for i, article in enumerate(articles, 1):
            print(f'{article["title"]}, posted {article["posted_time_ago"]}\n')