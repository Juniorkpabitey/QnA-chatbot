import os
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import OpenAI  # Assuming OpenAI is used; adjust if using Groq
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ['langchain_api_key'] = os.getenv("langchain_api_key")
os.environ['groq_api_key'] = os.getenv("groq_api_key")

# Define the prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Question: {question}")
])

# Generate response from model
def generate_response(question, engine, temperature, max_token):
    llm = OpenAI(api_key=os.getenv("langchain_api_key"))  # Replace with Groq if needed
    chain = prompt | llm  # Basic chain without parser
    answer = chain.invoke({"question": question})
    return answer

st.title("Juniorkpabitey_bot")
engine = st.sidebar.selectbox(
    "Select model",
    ["gemma2-9b-it", "llama3-groq-70b-8192-tool-use-preview", "llama-3.1-70b-versatile", "mixtral-8x7b-32768"]
)
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_token = st.sidebar.slider("Max Token", min_value=100, max_value=500, value=250)

# UI Input
st.write("Go ahead and ask your questions")
user_input = st.text_input("You:")
if user_input:
    response = generate_response(user_input, engine, temperature, max_token)
    st.write(response)
else:
    st.write("Provide an input")
