from llm.factory import LLMFactory
from cli.command import AskLLMCommand
from evaluation.strategy import LengthEvaluationStrategy, KeywordEvaluationStrategy, CombinedEvaluationStrategy

def cli():
    prompt = input("Digite sua pergunta aleatória: ")

    chatgpt_connection = LLMFactory.create_connection('chatgpt')
    gemini_connection = LLMFactory.create_connection('gemini')

    chatgpt_command = AskLLMCommand(chatgpt_connection, prompt)
    gemini_command = AskLLMCommand(gemini_connection, prompt)

    chatgpt_response = chatgpt_command.execute()
    gemini_response = gemini_command.execute()

    print(f"\nResposta ChatGPT: {chatgpt_response}")
    print(f"Resposta Google Gemini: {gemini_response}\n")

    keyword = "natal"  # Ajuste a palavra-chave conforme o contexto

    length_strategy = LengthEvaluationStrategy()
    keyword_strategy = KeywordEvaluationStrategy(keyword)

    combined_strategy = CombinedEvaluationStrategy([length_strategy, keyword_strategy])

    best_response = combined_strategy.evaluate(chatgpt_response, gemini_response)

    if best_response == chatgpt_response:
        best_model = "ChatGPT"
    else:
        best_model = "Google Gemini"

    print(f"Melhor resposta: {best_response} (Modelo: {best_model})")

if __name__ == "__main__":
    cli()
