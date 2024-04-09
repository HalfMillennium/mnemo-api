'''
File containing SearchResourceService that manages search resources and conducts page fetching.
'''
import requests
import asyncio
from mnemo_api.mnemo_logic.search.utils.search_tools.search_resources import WikiSearchResource, GoogleNewsSearchResource, YahooImagesSearchResource, AskRedditSearchResource
from ...page_parser.page_parser_service import PageParserService

class SearchResourceService:
    RESOURCES = {
        "Yahoo Images": YahooImagesSearchResource,
        "Google News": GoogleNewsSearchResource,
        "AskReddit": AskRedditSearchResource,
        "Wiki": WikiSearchResource
    }

    def __init__(self, resource_name = "Yahoo Images", time_frame_days = 7):
        self.resource_name = resource_name
        self.time_frame_days = time_frame_days
        SelectedResourceType = self.RESOURCES.get(self.resource_name)
        self.current_resource = SelectedResourceType()

    def build_query(self, prompt) -> str:
        return self.current_resource.build_query(prompt)

    async def execute_query(self, search_term) -> str:
        query_details = self.build_query(search_term)
        result = await self.__fetch_page_content(query_details)
        return result

    async def __fetch_page_content(self, url) -> str:
        response = requests.get(url)
        return response.text

    async def fetch_and_parse_images(self, search_term, alt = None, resource_name = "Yahoo Images"):
        page_html = await self.execute_query(search_term)
        yahoo_images_parser = PageParserService(resource_name, page_html)
        images = yahoo_images_parser.get_images() # { src: string, alt: string | None }[]
        return images

    '''
    Exposed for testing, should not be used directly
    '''
    def parse_response(self, responses):
        if responses == []:
            return None
        return responses[0].text if responses[0] else None