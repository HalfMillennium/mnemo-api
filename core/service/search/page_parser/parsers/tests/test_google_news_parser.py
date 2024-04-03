from .utils.example_html_snippet import ExampleHtmlSnippet
from ..google_news_parser import GoogleNewsParser

TEST_GET_STORIES_RESPONSE = {'title': "Travis Kelce covering pricey Super Bowl suite tab for his, Taylor Swift's families to sit together", 'source': 'Page Six', 'posted_time_ago': '4 hours ago'}

def test_google_news_parser():
    parser = GoogleNewsParser(ExampleHtmlSnippet.article_tag)
    stories_result = list(parser.get_stories())
    assert stories_result[0] == TEST_GET_STORIES_RESPONSE