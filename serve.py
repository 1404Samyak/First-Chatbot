

#Import OS
import os
from dotenv import load_dotenv
load_dotenv()


from langchain_ollama import OllamaLLM
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
model = OllamaLLM(model="gemma:2b")
parser=StrOutputParser()
chain=prompt_template|model|parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

