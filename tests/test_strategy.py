from evaluation.strategy import LengthEvaluationStrategy, KeywordEvaluationStrategy

def test_length_evaluation_strategy():
    strategy = LengthEvaluationStrategy()
    
    response1 = "Short response"
    response2 = "This is a much longer response than the first one."
    
    # Verifica se a resposta mais longa é retornada
    result = strategy.evaluate(response1, response2)
    
    assert result == response2

def test_keyword_evaluation_strategy():
    strategy = KeywordEvaluationStrategy(keyword="test")
    
    response1 = "This is a test. Testing keywords is fun."
    response2 = "No keyword here."
    
    # Verifica se a resposta com mais ocorrências da palavra-chave é retornada
    result = strategy.evaluate(response1, response2)
    
    assert result == response1

def test_keyword_evaluation_strategy_equal_counts():
    strategy = KeywordEvaluationStrategy(keyword="test")
    
    response1 = "Test this keyword here."
    response2 = "This test also has one test."
    
    result = strategy.evaluate(response1, response2)
    
    assert result == response2
