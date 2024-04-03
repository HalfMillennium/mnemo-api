from ..search_resources import WikiSearchResource, GoogleNewsSearchResource, YahooImagesSearchResource, AskRedditSearchResource
from ..utils import get_prior_and_current_date

EXAMPLE_PROMPT = "hello_world"

def test_wiki_news_resource():
    BASE_URL = WikiSearchResource.BASE_URL

    expected_query = f'{BASE_URL}?search={EXAMPLE_PROMPT}'

    wiki_search_resource = WikiSearchResource()
    assert wiki_search_resource.build_query(EXAMPLE_PROMPT) == expected_query

def test_google_news_search_resource():
    BASE_URL = GoogleNewsSearchResource.BASE_URL

    expected_query = f'{BASE_URL}?q={EXAMPLE_PROMPT}'

    google_search_resource = GoogleNewsSearchResource()
    assert google_search_resource.build_query(EXAMPLE_PROMPT) == expected_query


def test_yahoo_images_search_resource():
    BASE_URL = YahooImagesSearchResource.BASE_URL

    expected_query = f'{BASE_URL};?p={EXAMPLE_PROMPT}'

    yahoo_search_resource = YahooImagesSearchResource()
    assert yahoo_search_resource.build_query(EXAMPLE_PROMPT) == expected_query

def test_ask_reddit_search_resource():
    BASE_URL = AskRedditSearchResource.BASE_URL

    expected_query = f'{BASE_URL}?q={EXAMPLE_PROMPT}'

    ask_reddit_search_resource = AskRedditSearchResource()
    assert ask_reddit_search_resource.build_query(EXAMPLE_PROMPT) == expected_query

