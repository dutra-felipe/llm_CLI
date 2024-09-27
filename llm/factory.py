from llm.connection import ChatGPTConnection, GeminiConnection

class LLMFactory:
    @staticmethod
    def create_connection(llm_type):
        if llm_type == 'chatgpt':
            return ChatGPTConnection()
        elif llm_type == 'gemini':
            return GeminiConnection()
        else:
            raise ValueError("Modelo não suportado")
