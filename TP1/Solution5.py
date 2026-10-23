# ==========================================
# Problem 5: Letter Grade (Medium)
# ==========================================

def letter_grade(score):
    """Returns the letter grade for a given score based on the grading scale."""
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 97:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Part (a): Test the function with the list and print results
print("\n--- Problem 5(a) Tests ---")
test_scores = [99, 90, 85.5, 72, 60, 59.9, -5, 101]
for s in test_scores:
    print(f"{s} -> {letter_grade(s)}")