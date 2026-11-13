import json
model = {
    "name": "Gemini",
    "provider": "Google",
    "temperature": 0.5,
    "max_tokens": 4000
}
with open("model_config.json", "w") as file:
    json.dump(model, file, indent=4)

with open("model_config.json", "r") as file:
    loaded_model = json.load(file)
    print("Model Name:", loaded_model["name"])
    print("Provider:", loaded_model["provider"])