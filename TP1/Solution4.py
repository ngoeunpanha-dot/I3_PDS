# ==========================================
# Problem 4: Type-Conversion Detective (Medium)
# Part B & C: safe_int and User Input Sum
# ==========================================

def safe_int(text):
    """Turns a string into an int. Accepts spaces, negative numbers, and decimals."""
    if not isinstance(text, str):
        return None
    try:
        # Strip whitespace and convert via float to handle decimals (e.g., "3.9" -> 3.9 -> 3)
        return int(float(text.strip()))
    except (ValueError, TypeError):
        return None

# Testing Part B (matches expected output)
print("--- Problem 4B Tests ---")
for sample in ["42", " -8 ", "3.9", "abc", ""]:
    print(f"{repr(sample)} -> {safe_int(sample)}")


# Part C: Ask the user for two numbers, convert, and print their sum
def add_user_numbers():
    num1_str = input("\nEnter first number: ")
    num2_str = input("Enter second number: ")
    
    val1 = safe_int(num1_str)
    val2 = safe_int(num2_str)
    
    if val1 is not None and val2 is not None:
        print(f"The sum is: {val1 + val2}")
    else:
        print("Friendly message: One or both of the inputs are not valid numbers!")