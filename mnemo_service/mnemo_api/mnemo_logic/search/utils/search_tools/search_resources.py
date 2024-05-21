'''
File containing all SearchResource classes
'''
from ...utils.search_tools.types.search_resource import SearchResource

class GoogleNewsSearchResource(SearchResource):
    BASE_URL = "https://news.google.com/search"
    SOURCE_NAME = "Google News Search"

    def build_query(self, prompt):
        query = f'{self.BASE_URL}?q={prompt}'
        print(f'BUILT [{self.SOURCE_NAME}] QUERY: "{query}"')
        return query
        
    def __str__(self):
        return self.SOURCE_NAME

    def parse_page_stories(raw_html):
        pass

class WikiSearchResource(SearchResource):
    BASE_URL = "https://en.wikipedia.org/w/index.php"
    SOURCE_NAME = "Wiki Search"

    def build_query(self, prompt):
        query = f'{self.BASE_URL}?search={prompt}'
        print(f'BUILT [{self.SOURCE_NAME}] QUERY: "{query}"')
        return query
        
    def __str__(self):
        return self.SOURCE_NAME

class YahooImagesSearchResource(SearchResource):
    BASE_URL = "https://images.search.yahoo.com/search/images"
    SOURCE_NAME = "Yahoo Images Search"

    def build_query(self, prompt):
        query = f'{self.BASE_URL};?p={prompt}'
        print(f'BUILT [{self.SOURCE_NAME}] QUERY: "{query}"')
        return query
        
    def __str__(self):
        return self.SOURCE_NAME


class AskRedditSearchResource(SearchResource):
    BASE_URL = "https://www.reddit.com/r/AskReddit/search"
    SOURCE_NAME = "Reddit Search"

    def __init__(self, sort = "hot"):
        self.sort = sort

    def build_query(self, prompt):
        query = f'{self.BASE_URL}?q={prompt}'
        print(f'BUILT [{self.SOURCE_NAME}] QUERY: "{query}"')
        return query
        
    def __str__(self):
        return self.SOURCE_NAME