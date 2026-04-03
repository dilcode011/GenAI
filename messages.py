#Messages
#This file contains all the messages that are used in the bot. This is to make it easier to manage the messages and to make it easier to translate the bot to other languages.

#! TYPES OF MESSAGES    
#System messages
#These messages are used for system notifications and errors.

#Human messages
#These messages are used for human interactions and responses.

#AI messages
#These messages are used for AI interactions and responses.


from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

model=ChatOpenAI()
messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='what is the capital of france?'),
]

result=model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)