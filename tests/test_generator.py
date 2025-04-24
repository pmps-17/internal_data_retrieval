import pytest
from app import generator

# Dummy classes to mimic OpenAI response
class DummyMessage:
    def __init__(self, content):
        self.content = content

class DummyChoice:
    def __init__(self, content):
        self.message = DummyMessage(content)

class DummyResponse:
    def __init__(self, content):
        self.choices = [DummyChoice(content)]

# Dummy client that stitches together the .chat.completions.create(...) chain
class DummyClient:
    def __init__(self, resp_content):
        self._resp = resp_content
        self.chat = self
        self.completions = self

    def create(self, **kwargs):
        return DummyResponse(self._resp)

@pytest.fixture(autouse=True)
def patch_openai(monkeypatch):
    dummy = DummyClient("This is a concise answer.")
    monkeypatch.setattr(generator, 'client', dummy)
    return dummy

def test_generate_answer_returns_dummy(monkeypatch):
    query = "How to reset password?"
    contexts = [
        {"metadata": {"text": "Step 1: Go to settings."}},
        {"metadata": {"text": "Step 2: Click 'Reset'."}}
    ]
    answer = generator.generate_answer(query, contexts)
    assert answer == "This is a concise answer."
