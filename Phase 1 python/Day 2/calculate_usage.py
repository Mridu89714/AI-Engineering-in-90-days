def calculate_usage(used_tokens, total_tokens):
    percentage = (used_tokens / total_tokens) * 100
    return percentage
result =calculate_usage(4000, 8000)
print(f"Total usage:{result:.2f}%")
