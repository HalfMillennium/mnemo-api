'''
Parsing library for Google News search results
'''
from bs4 import BeautifulSoup

class GoogleNewsParser:
    def __init__(self, raw_html):
        self.page_soup = self.__make_soup(raw_html)
        self.raw_html = raw_html

    def __make_soup(self, raw_html):
        return BeautifulSoup(raw_html, 'html.parser')

    def __fetch_story_details(self, article_element):
        sub_contents = article_element

        title_element = sub_contents.find('a', attrs={"data-n-tid": "29"})
        title = title_element.text if title_element else None
        
        posted_time_ago_element = sub_contents.find('time')  # Assuming the posted time is always within a time tag
        posted_time_ago = posted_time_ago_element.text if posted_time_ago_element else ''

        source_element = sub_contents.find('div', attrs={"data-n-tid": "9"})
        source = source_element.text if source_element else None
        
        return {'title': title, 'source': source, 'posted_time_ago': posted_time_ago}

    def get_stories(self):
        article_elements = self.page_soup.find_all('article')

        for element in article_elements:
            element_details = self.__fetch_story_details(element)
            yield element_details
                        