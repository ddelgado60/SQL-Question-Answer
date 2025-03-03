import streamlit as st
import torch
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(project_root))
st.set_page_config(layout="wide")
torch.classes.__path__ = []

from src.utils.model_load import get_model, get_tokenizer
from src.utils.utils import format_input, generate_sql, format_sql

st.title("SQL Generator App")

model_name = "DevD60/sql_generator_f5"

model = get_model(model_name)
tokenizer = get_tokenizer(model_name)

col1, col2 = st.columns([3, 2], gap="large")

question = col1.text_input("Enter a question")
context = col1.text_area("Enter the context", height=400)

col2_placeholder = col2.empty()
col2_placeholder.markdown("<p style='text-align: center; color: orange;'> Generated SQL will appear here </p>", unsafe_allow_html=True)

if st.button("Generate SQL"):
    inputs = format_input(question, context, tokenizer)
    generated_sql = generate_sql(inputs, model, tokenizer)
    formatted_sql = format_sql(generated_sql)
    
    col2_placeholder.write(f"```sql\n{formatted_sql}\n```")