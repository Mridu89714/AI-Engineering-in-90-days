# print("Welcome to prompt analyzer!")
# prompt = input("Enter you prompt: ")


# character_count = len(prompt)
# word_count = len(prompt.split())

# print("Prompt Analysis...")
# print(prompt)
# print(character_count)
# print(word_count)

# if prompt.strip():
#     print("Your prompt is valid")
# else:
#     print("Your prompt is invalid")


prompt = input("Enter your prompt: ")
if prompt.strip() == "":
    print("Your prompt is invalid")
else:
    character_count = len(prompt)
    word_count = len(prompt.split())

    print("Prompt Analysis...")
    print(f"Prompt: {prompt}")
    print(f"Character Count: {character_count}")
    print(f"Word Count: {word_count}")