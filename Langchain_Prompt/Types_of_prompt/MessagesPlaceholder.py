from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat = ChatPromptTemplate.from_messages([
    ("system", "You are helpful"),
    MessagesPlaceholder(variable_name="history"),
    ("user", "{input}")
])