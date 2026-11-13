import json

models = {
    "GPT": {
        "provider": "OpenAI",
        "temperature": 0.7,
        "max_tokens": 8000
    },
    "Gemini": {
        "provider": "Google",
        "temperature": 0.5,
        "max_tokens": 4000
    },
    "Claude": {
        "provider": "Anthropic",
        "temperature": 0.3,
        "max_tokens": 6000
    }
}
with open("ai_models.json", "w") as file:
    json.dump(models, file, indent=4)

with open("ai_models.json", "r") as file:
    loaded_models=json.load(file)

model_name = input("Enter model name: ")
if model_name in loaded_models:
    new_temp = float(input("Enter new temperature: "))
    if 0 <= new_temp <= 2:
        loaded_models[model_name]["temperature"] = new_temp
        print("Temperature updated")
    else:
        print("Invalid temperature!")
with open("ai_models.json", "w") as file:
    json.dump(loaded_models, file, indent=4)

print("------ AI Models Configuration ---")
for name, config in loaded_models.items():
    print(f"Model: {name}")
    print(f"Provider: {config['provider']}")
    print(f"Temperature: {config['temperature']}")
    print(f"Max Tokens: {config['max_tokens']}")
