from .utils.example_html_snippet import ExampleHtmlSnippet
from ..yahoo_images_parser import YahooImagesParser

TEST_PARSE_IMAGES_RESULT = [
    {'src': 'https://s.yimg.com/fz/api/res/1.2/_RxOK6.QSs2yYSjmERVvSA--~C/YXBwaWQ9c3JjaGRkO2ZpPWZpbGw7aD04ODt3PTg4/https://tse3.mm.bing.net/th?q=John+Malkovich+Kids&pid=Api&mkt=en-US&cc=US&setlang=en&adlt=strict&t=1', 'alt': 'john malkovich Kids'},
    {'src': 'https://s.yimg.com/fz/api/res/1.2/HtwfdYZ14d4h9msiMDkSbw--~C/YXBwaWQ9c3JjaGRkO2ZpPWZpbGw7aD04ODt3PTg4/https://tse2.mm.bing.net/th?q=Glenne+Headly+John+Malkovich&pid=Api&mkt=en-US&cc=US&setlang=en&adlt=strict&t=1', 'alt': 'Glenne Headly john malkovich'},
    {'src': 'https://s.yimg.com/fz/api/res/1.2/lVuSJu7JYcBdEidFIVALXQ--~C/YXBwaWQ9c3JjaGRkO2ZpPWZpbGw7aD04ODt3PTg4/https://tse4.mm.bing.net/th?q=John+Malkovich+Johnny+English&pid=Api&mkt=en-US&cc=US&setlang=en&adlt=strict&t=1', 'alt': 'john malkovich Johnny English'}
]

def test_yahoo_images_parser():
    parser = YahooImagesParser(ExampleHtmlSnippet.images_html)
    images_result = list(parser.get_images())
    assert images_result == TEST_PARSE_IMAGES_RESULT