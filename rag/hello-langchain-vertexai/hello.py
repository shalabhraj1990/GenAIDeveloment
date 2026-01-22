from langchain.chat_models import init_chat_model


if __name__ == "__main__":
    gemini_llm = init_chat_model("gemini-2.5-flash-lite",model_provider="google_vertexai")
    response = gemini_llm.invoke("what is capital of inida")
    response.pretty_print()
