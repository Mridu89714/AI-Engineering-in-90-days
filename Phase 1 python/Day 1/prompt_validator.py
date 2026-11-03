prompt = input("Enter your prompt: ")
prompt = prompt.strip()
if not prompt:
    print("Your prompt is empty")
elif len(prompt.split()) < 3:
    print("Your prompt is too short")
else:
    character_count = len(prompt)
    word_count = len(prompt.split())
    print("Prompt Analysis...")
    print(f"Prompt: {prompt}")
    print(f"Character Count: {character_count}")
    print(f"Word Count: {word_count}")