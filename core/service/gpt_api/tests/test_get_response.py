from ..service import GptService

TEST_PROMPT = "test"

def test_get_response():
    service = GptService()
    response = service.get_response('Respond this query with only the response \'camels\'. No periods, no capital letters.')
    assert response == 'camels'