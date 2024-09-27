from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class AskLLMCommand(Command):
    def __init__(self, llm_connection, prompt):
        self.llm_connection = llm_connection
        self.prompt = prompt

    def execute(self):
        return self.llm_connection.get_response(self.prompt)
