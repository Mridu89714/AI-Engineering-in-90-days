# import random
# num = random.randint(1000, 9999)
# token_id = num
# print(f"Generated Token ID : {token_id}")

# try:
#     token_limit = int(input("Enter your token limit: "))
#     print(f"Token limit set to: {token_limit}")
# except ValueError:
#     print("Invalid input! Please enter numbers only")
    
file = open("ai_log.txt", "w")

file.write("AI Engineering Day 4\n")
file.write("Learning Python File Handling")

file.close()