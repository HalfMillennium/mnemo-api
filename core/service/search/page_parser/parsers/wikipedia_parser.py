'''
Parsing library for Wikipedia search results
'''
from bs4 import BeautifulSoup

class WikipediaParser:
    def __init__(self, raw_html):
        self.page_soup = self.__make_soup(raw_html)
        self.raw_html = raw_html

    def __make_soup(self, raw_html):
        return BeautifulSoup(raw_html, 'html.parser')
    
    def get_paragraphs(self):
        for result in self.page_soup.find_all('p'):
            yield result.get_text()