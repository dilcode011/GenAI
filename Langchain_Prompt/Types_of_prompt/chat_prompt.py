from langchain_core.prompts import ChatPromptTemplate

chat = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Explain {topic}")
])

print(chat.format_messages(topic="Machine Learning"))