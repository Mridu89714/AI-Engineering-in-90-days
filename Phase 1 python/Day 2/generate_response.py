def generate_response(prompt, temp=0.7):
    return f"Prompt: {prompt}\n Temperature: {temp}"
print(generate_response("Explain Machine learning"))
print(generate_response("Explain Deep learning", 0.2))