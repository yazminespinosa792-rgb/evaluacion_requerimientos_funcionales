from ollama import chat

pregunta = input("En que te purdo ayudar")

response = chat(
    model ='llama3.2:3b',
    messages =[
            {'role': 'user', 
             'content': 'f"Responde a la siguiente pregunta como si fueras mario bros: {pregunta}"'
            }
        ],
)
print(response.message.content)