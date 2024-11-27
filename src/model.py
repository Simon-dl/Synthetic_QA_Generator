import ollama


model = ollama.Model(model="llama3.2")
modelcard = model.card()
print(modelcard)
