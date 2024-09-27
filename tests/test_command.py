from cli.command import AskLLMCommand
from unittest.mock import MagicMock

def test_ask_llm_command():
    mock_llm_connection = MagicMock()
    mock_llm_connection.get_response.return_value = "Simulated response"
    
    command = AskLLMCommand(mock_llm_connection, "Test prompt")
    
    result = command.execute()
    
    assert result == "Simulated response"
    
    mock_llm_connection.get_response.assert_called_once_with("Test prompt")
