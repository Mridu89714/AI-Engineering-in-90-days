tokens = 8000
print("Maximum tokens available:", tokens)
used_tokens = int(input("Enter the number of tokens used: "))
print("Used tokens", used_tokens)
remaining_tokens = tokens - used_tokens
print("Remaining tokens:", remaining_tokens)
usage_percentage = (used_tokens / tokens) * 100
print("Usage percentage:", usage_percentage, "%")
if usage_percentage >= 50:
    print("Token usage is above 50%")
else:
    print("Token usage is below 50%")