from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm=OpenAI(model_name='gpt-3.5-turbo',temperature=0.7)

prompt=PromptTemplate(
    template='suggest a catchy blog title about {topic}',
    input_Variables=['topic']
)

#define a input
topic=input('Enter a topic :')

#format the prompt manually using prompttemplate
formatted_prompt=prompt.format(topic=topic)

#call the llm directly
blog_title=llm.predict(formatted_prompt)

#print the output
print('generate blog title:',blog_title)