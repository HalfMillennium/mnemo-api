from .parsers.google_news_parser import GoogleNewsParser
from .parsers.yahoo_images_parser import YahooImagesParser

class PageParserService:
    PARSERS = {
        "Google News": GoogleNewsParser,
        "Yahoo Images": YahooImagesParser
        # Create and add others
    }

    def __init__(self, resource, raw_html):
        self.resource = resource
        self.raw_html = raw_html
        self.parser = self.PARSERS.get(self.resource)(self.raw_html)

    def get_stories(self):
        if(self.resource != "Google News"):
            raise Exception(f'{self.resource} does not implement \'get_stories()\' method.')
        return self.parser.get_stories()

    def get_images(self, alt = None):
        if(self.resource != "Yahoo Images"):
            raise Exception(f'{self.resource} does not implement \'get_images()\' method.')
        return self.parser.get_images(alt)
    