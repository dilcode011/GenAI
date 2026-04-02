from langchain_openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

load_dotenv()

model=OpenAI(model='gpt-3.5-turbo')
st.header('Research Tool')
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# Load the prompt template from the JSON file created in prompt_gentr.py
template = load_prompt('template.json')


# When the "Summarize" button is clicked, the code creates a chain by combining the loaded prompt template with the language model. It then invokes the chain with the user inputs (paper name, explanation style, and explanation length) to generate a summary of the research paper. The result is displayed on the Streamlit app using st.write().
if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.content)