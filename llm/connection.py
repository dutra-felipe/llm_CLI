from abc import ABC, abstractmethod
import openai
import google.generativeai as genai

class LLMConnection(ABC):
    @abstractmethod
    def get_response(self, prompt):
        pass

class ChatGPTConnection(LLMConnection):
    def get_response(self, prompt):
        openai.api_key = 'coloque a sua API-KEY' #colocar a API KEY do GPT aqui
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()

class GeminiConnection(LLMConnection):
    def __init__(self):
        genai.configure(api_key='coloque a sua API-KEY') #colocar a API KEY do GEMINI aqui

    def get_response(self, prompt):
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content([prompt])

            if response and hasattr(response, 'text'):
                return response.text.strip()
            else:
                return "Nenhuma resposta gerada."
        except Exception as e:
            return f"Erro: {e}"
