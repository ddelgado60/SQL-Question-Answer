import streamlit as st
import torch
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(project_root))

torch.classes.__path__ = []
from src.utils.model_load import get_model, get_tokenizer
from src.utils.utils import format_input, generate_sql, format_sql

st.title("SQL Generator App")

model_name = "DevD60/sql_generator_f5"

model = get_model(model_name)
tokenizer = get_tokenizer(model_name)

question = st.text_input("Enter a question")
context = st.text_area("Enter the context")

if st.button("Generate SQL"):
    inputs = format_input(question, context, tokenizer)
    generated_sql = generate_sql(inputs, model, tokenizer)
    formatted_sql = format_sql(generated_sql)
    st.write(f"```sql\n{formatted_sql}\n```")