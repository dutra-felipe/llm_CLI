from abc import ABC, abstractmethod

class EvaluationStrategy(ABC):
    @abstractmethod
    def evaluate(self, response1, response2):
        pass

class LengthEvaluationStrategy(EvaluationStrategy):
    def evaluate(self, response1, response2):
        return response1 if len(response1) > len(response2) else response2

class KeywordEvaluationStrategy(EvaluationStrategy):
    def __init__(self, keyword):
        self.keyword = keyword

    def evaluate(self, response1, response2):
        count1 = response1.lower().count(self.keyword.lower())
        count2 = response2.lower().count(self.keyword.lower())

        if count1 > count2:
            return response1
        elif count2 > count1:
            return response2
        return response2

class CombinedEvaluationStrategy(EvaluationStrategy):
    def __init__(self, strategies):
        self.strategies = strategies

    def evaluate(self, response1, response2):
        score1, score2 = 0, 0

        for strategy in self.strategies:
            result = strategy.evaluate(response1, response2)
            if result == response1:
                score1 += 1
            elif result == response2:
                score2 += 1

        return response1 if score1 > score2 else response2
