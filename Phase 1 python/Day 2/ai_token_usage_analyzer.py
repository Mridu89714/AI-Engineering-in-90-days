total_tokens = int(input("Enter total token capacity: "))
used_tokens = int(input("Enter tokens consumed: "))

def calculate_usage(used_tokens, total_tokens):
    percent = (used_tokens / total_tokens) * 100
    return percent

def get_status(percent):
    if percent <=0:
        return "Invalid usage percentage"
    elif percent <30:
        return "Low usage"
    elif percent <=70:
        return "Moderate usage"
    elif percent >70 and percent <80:
        return "High usage"
    else:
        return "Warning: Your are approaching your token limit!"
    
def generate_report(used_tokens, total_tokens):
    percent = calculate_usage(used_tokens, total_tokens)
    status = get_status(percent)
    return f"Total usage: {percent:.2f}%\nStatus: {status}"

print("----- AI Token Usage Report -----")
print(f"Total capacity: {total_tokens}")
print(f"Tokens used: {used_tokens}")
print(f"Remaining tokens: {total_tokens - used_tokens}")
print(f"Usage percentage: {calculate_usage(used_tokens, total_tokens):.2f}%")
print(f"Status: {get_status(calculate_usage(used_tokens, total_tokens))}")
print(get_status(calculate_usage(used_tokens, total_tokens)))

def calculate_usage(used_tokens, total_tokens):
    return (used_tokens / total_tokens) * 100


def get_status(percent):
    if percent < 30:
        return "Low Usage"
    elif percent <= 70:
        return "Moderate Usage"
    else:
        return "High Usage"

#optimized version of the code
# def generate_report(used_tokens, total_tokens):

#     percent = calculate_usage(used_tokens, total_tokens)
#     remaining = total_tokens - used_tokens
#     status = get_status(percent)

#     print("\n----- AI TOKEN USAGE REPORT -----")
#     print(f"Total Capacity: {total_tokens}")
#     print(f"Tokens Used: {used_tokens}")
#     print(f"Remaining Tokens: {remaining}")
#     print(f"Usage Percentage: {percent:.2f}%")
#     print(f"Status: {status}")

#     if percent > 80:
#         print("Warning: You are approaching your token limit!")


# total_tokens = int(input("Enter total token capacity: "))
# used_tokens = int(input("Enter tokens consumed: "))

# if total_tokens <= 0:
#     print("Invalid token capacity")

# elif used_tokens < 0 or used_tokens > total_tokens:
#     print("Invalid token usage")

# else:
#     generate_report(used_tokens, total_tokens)