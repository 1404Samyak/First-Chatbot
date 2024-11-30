# Now that we've built an application, we need to serve it. That's where LangServe comes in. LangServe helps developers deploy LangChain chains as a REST API. You do not need to use LangServe to use LangChain, but in this guide we'll show how you can deploy your app with LangServe.

# While the first part of this guide was intended to be run in a Jupyter Notebook or script, we will now move out of that. We will be creating a Python file and then interacting with it from the command line.

#Import OS
import os
from dotenv import load_dotenv
load_dotenv()


from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

#Langsmith serving
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

prompt_template=ChatPromptTemplate.from_messages(
    [("system","You are a helpful assistant so pls respond to the question asked"),("user","Question:{question}")]
)

#Streamlit framework
st.title("Langchain demo with an open source GEMMA:2b model")
input_text=st.text_input("What question do u have in your mind")

#ollama 
model=Ollama(model='gemma:2b')
parser=StrOutputParser()
chain=prompt_template|model|parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

