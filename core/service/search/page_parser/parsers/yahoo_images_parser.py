'''
Parsing library for Yahoo Images search results
'''
from bs4 import BeautifulSoup

class YahooImagesParser:
    def __init__(self, raw_html):
        self.page_soup = self.__make_soup(raw_html)
        self.raw_html = raw_html

    def __make_soup(self, raw_html):
        return BeautifulSoup(str(raw_html), 'html.parser')

    def get_images(self):
        for img in self.page_soup.find_all('img'):
            if(img.get('alt')):
                yield { 'src': img.get('src'), 'alt': img.get('alt') }

    def get_stories(self):
        article_elements = self.page_soup.find_all('article')

        for element in article_elements:
            element_details = self.__fetch_story_details(element)
            yield element_details
                        