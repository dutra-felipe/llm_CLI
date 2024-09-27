import pytest
from llm.factory import LLMFactory
from llm.connection import ChatGPTConnection, GeminiConnection

def test_create_chatgpt_connection():
    connection = LLMFactory.create_connection('chatgpt')
    assert connection is not None
    assert isinstance(connection, ChatGPTConnection)

def test_create_gemini_connection():
    connection = LLMFactory.create_connection('gemini')
    assert connection is not None
    assert isinstance(connection, GeminiConnection)

def test_invalid_model():
    with pytest.raises(ValueError):
        LLMFactory.create_connection('invalid')
