from abc import ABC, abstractmethod

class EvaluationStrategy(ABC):
    @abstractmethod
    def evaluate(self, response1, response2):
        pass

class LengthEvaluationStrategy(EvaluationStrategy):
    def evaluate(self, response1, response2):
        score1 = len(response1)
        score2 = len(response2)
        return score1, score2

class KeywordEvaluationStrategy(EvaluationStrategy):
    def __init__(self, keyword):
        self.keyword = keyword

    def evaluate(self, response1, response2):
        count1 = response1.count(self.keyword)
        count2 = response2.count(self.keyword)
        return count1, count2

class CombinedEvaluationStrategy(EvaluationStrategy):
    def __init__(self, strategies):
        self.strategies = strategies

    def evaluate(self, response1, response2):
        score1, score2 = 0, 0

        for strategy in self.strategies:
            strategy_score1, strategy_score2 = strategy.evaluate(response1, response2)
            score1 += strategy_score1
            score2 += strategy_score2

        return response1 if score1 > score2 else response2
