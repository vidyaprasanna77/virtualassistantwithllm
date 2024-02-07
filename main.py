import datetime
from playsound import playsound
import wikipedia

from transformers import AutoModelForQuestionAnswering, AutoModelForSeq2SeqLM

# Choose the appropriate model class based on your chosen Hugging Face model
model = AutoModelForQuestionAnswering.from_pretrained("mistralai/Mistral-7B-v0.1")


# defining the llm function
def llm_query(prompt):
    # Use the Hugging Face model to process the prompt and generate a response
    inputs = tokenizer(prompt, return_tensors="pt")
    generated_text = model.generate(**inputs)[0]
    # outputs = model(**inputs)
    # Extract the relevant output (e.g., generated text, answer)
    # response = ...
    return generated_text.strip()
