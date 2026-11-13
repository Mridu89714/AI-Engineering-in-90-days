with open("token_report.txt", "w") as file:
    file.write("AI Model: GPT\n")
    file.write("Token Limit: 8000\n")
    file.write("Tokens Used: 2500\n")

with open("token_report.txt", "r") as file:
    content = file.read()
    print(content)