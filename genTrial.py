import pathlib
import textwrap
import os
import google.generativeai as genai

# Used to securely store your API key

from dotenv import dotenv_values
from IPython.display import display
from IPython.display import Markdown

env_vars = dotenv_values(".env")
# GOOGLE_API=os.getenv('GOPATH')
# to do : add google_api_key  in os env var 
GOOGLE_API_KEY=env_vars.get('GOOGLE_API_KEY') 

# print(GOOGLE_API)
genai.configure(api_key=GOOGLE_API_KEY)

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))



model = genai.GenerativeModel('gemini-pro')

commandPrompt = "Show command for the given query. Show only command not any other description with it. Also show text as 'invalid input' if user provide wrong information."
userInput = "open file named vp"

response = model.generate_content(commandPrompt + userInput)

output = to_markdown(response.text)
display(response.text)
print(response.text)

