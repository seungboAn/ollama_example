

import ollama

user_input = input("Ask follow-up: ")

response = ollama.chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': user_input,
  },
])
print(response['message']['content'])