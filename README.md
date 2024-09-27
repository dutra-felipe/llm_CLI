# LLM Command Line Interface

Este projeto é uma interface de linha de comando (CLI) para fazer perguntas a modelos de linguagem como ChatGPT (OpenAI) e Google Gemini. Ele permite comparar as respostas de ambos os modelos usando uma estratégia de avaliação personalizada.

## Funcionalidades

- **Comandos LLM**: Faz perguntas tanto ao ChatGPT quanto ao modelo Google Gemini usando a classe `AskLLMCommand`.
- **Estratégias de Avaliação**: Utiliza a `KeywordEvaluationStrategy` para determinar qual resposta é melhor com base em uma palavra-chave fornecida.
- **Padrão Observer**: Notifica observadores quando novas respostas estão disponíveis.
- **Fábrica de Conexões LLM**: Usa o padrão de projeto `Factory` para criar instâncias de conexão com os modelos de linguagem (ChatGPT e Google Gemini).

## Requisitos

Antes de executar o projeto, certifique-se de que as seguintes dependências estejam instaladas. As dependências estão listadas no arquivo `requirements.txt`.

### Dependências principais

- `openai==0.28.0`
- `google-generativeai==0.8.2`
- `pytest==8.3.3`

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/dutra-felipe/llm_CLI.git

2. **Navegue até o diretório do projeto**:
    ```bash
    cd llm_CLI

3. **Crie e ative um ambiente virtual e instale as dependências**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

## OBSERVAÇÃO

Para rodar o código é necessário gerar a Google Gemini API Key e a OpenAI API Key e substituí-las no arquivo main.py

[OpenAI API Key](https://platform.openai.com/api-keys)

[Google Gemini API Key](https://developers.generativeai.google)

Após adquirir as chaves, rodar o comando `main.py` no terminal para rodar o programa!