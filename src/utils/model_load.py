from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import streamlit as st

@st.cache_resource
def get_model(model_name):
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name, trust_remote_code=True)
    return model

@st.cache_resource
def get_tokenizer(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    return tokenizer