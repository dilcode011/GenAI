#A MessagePlaceholder in LangChain is a special type of message that serves as a placeholder for dynamic content in a conversation. It allows you to define a message template with variables that can be filled in at runtime. This is particularly useful when you want to create a conversation flow that can adapt based on user input or other dynamic factors.

#For example, you can create a MessagePlaceholder for a system message that includes a variable for the user's name. When the conversation is invoked, you can fill in the user's name dynamically, and the message will be generated accordingly.

#It is used inside ChatPromptTemplate to create dynamic prompts that can change based on the context of the conversation. This allows for more flexible and personalized interactions with the AI model.

from langchain_core.prompts import ChatPromptTemplate,MessagePlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

#chat template
chat_template=ChatPromptTemplate([
    ('system','You are a helpful customer assistant agent'),
    MessagePlaceholder(variable_name='chat_history'),
    ('human','{query}')
])


chat_history=[]
#load chat history
with open('chat_history.txt','r') as f:
    chat_history.extend(f.readlines())
    
    print(chat_history)
    
#create prompt
prompt=chat_template.invoke({'chat_history':chat_history,'query':'What is the return policy?'})
print(prompt)