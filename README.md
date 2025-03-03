# Sequence-to-Sequence SQL Generator

This repository sets up a Streamlit application to generate SQL queries based on a fine-tuned version of t5-small. 


Details on the model can be found on [Hugging Face](https://huggingface.co/DevD60/sql_generator_f5).

## Setup Steps

Ensure you have Anaconda installed. Then, from the terminal, run `conda create --name sql_generator --file requirements.txt`.
To run the application, run `streamlit run src/app/Generator.py` from the root directory.