
models = {
    "GPT": {"temperature": 0.7},
    "Gemini": {"temperature": 0.5},
    "Claude": {"temperature": 0.3},
    "Mistral": {"temperature": 0.8},
    "Llama": {"temperature": 0.9}
}
count = 0
for m in models:
    if models[m]["temperature"] > 0.5:
        count+=1
        print(m)
print(f"Number of models with temperature greater than 0.5: {count}")