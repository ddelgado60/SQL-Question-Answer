from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import sqlparse

def format_input(question: str, context: str, tokenizer: AutoTokenizer) -> str:
    '''
    Formats the question and context for the model to generate a SQL query.

    Args:
        question (str): The question to ask the model
        context (str): The context to provide the model
        model (transformers.AutoModelForSeq2SeqLM): The model to generate the SQL query
        tokenizer (transformers.AutoTokenizer): The tokenizer to format the input for the model

    Returns:
        str: The formatted question and context
    '''
    input_text = f"Translate to SQL: {question} Context: {context}"
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True, max_length=512)

    return inputs

def generate_sql(inputs: str, model: AutoModelForSeq2SeqLM, tokenizer: AutoTokenizer) -> str:
    '''

    Args:
        inputs (str): Input question and context to generate SQL query
        model (AutoModelForSeq2SeqLM): The model to generate the SQL query
        tokenizer (AutoTokenizer): The tokenizer to format the input for the model

    Returns:
        str: Generated SQL query 
    '''
    output_ids = model.generate(**inputs, max_length=512, do_sample=True, temperature=0.6, top_k=50, top_p=0.95)
    generated_sql = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    return generated_sql

def format_sql(sql: str) -> str:
    '''
    Formats the SQL query for better readability.

    Args:
        sql (str): The SQL query to format

    Returns:
        str: The formatted SQL query
    '''
    formatted_sql = sqlparse.format(sql, reindent=True, keyword_case='upper')
    
    return formatted_sql