from .utils.example_html_snippet import ExampleHtmlSnippet
from ..wikipedia_parser import WikipediaParser

TEST_PARSE_PARAGRAPHS_RESULT = [
    'Paragraph content Of Mice and Men',
    'More paragraph content'
]

def test_wikipedia_parser():
    parser = WikipediaParser(ExampleHtmlSnippet.paragraphs_html)
    paragraphs_result = list(parser.get_paragraphs())
    assert paragraphs_result == TEST_PARSE_PARAGRAPHS_RESULT

def test_wikipedia_parser_empty():
    parser = WikipediaParser('')
    paragraphs_result = list(parser.get_paragraphs())
    assert paragraphs_result == []

def test_wikipedia_parser_none():
    paragraphs_result = []
    try:
        parser = WikipediaParser(None)
        paragraphs_result = list(parser.get_paragraphs())
        assert False
    except:
        assert paragraphs_result == []