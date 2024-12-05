import os

#
os.environ['langchain_api_key']= os.getenv("langchain_api_key")

prompt= ChatPromptTemplate.from_message(
    [
        ("system","You are a helpful assistant"),
        ("user","question: {question}")
    ]
)

def chat_response(question, engine, temperature, max_token):
llm= OpenAI(api_key=os.getenv("langchain_api_key"))
chain = prompt | llm
answer = chain.invoke({"question": question})
return answer

st.title("Welcome to QnA")
engine = st.sidebar.selectbox("select Model:", ["123","12323","2232"])

temperature = st.slider(min_value = 0.1, max_value=5.0)
max Token= st.slider(min_value=100, max_value=1234)
st.write("enter a prompt")
user_input = st.text_input("you:")
if user_input:
    response = chat_response(user_input,engine, temperature, max_token)
    st.write(response)
else:
    st.write("provide an input")