
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

for name in models:
    print(f"Model: {name}")

print(f"Total models: {len(models)}")

selected_model = input("\nEnter model name: ").strip()

if selected_model in models:

    # Display configuration

    new_temperature = float(input("\nEnter new temperature: "))

    if 0 <= new_temperature <= 2:
        models[selected_model]["temperature"] = new_temperature
        print("Temperature updated successfully!")
    else:
        print("Invalid temperature!")

else:
    print("Model not found!")