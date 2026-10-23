# ---------------------------------------------------------------------------
# Problem 3 (Easy) · Temperature converter
# ---------------------------------------------------------------------------
def celsius_to_fahrenheit(c, round_to=1):
    """Convert degrees Celsius to degrees Fahrenheit."""
    return round(c * 9 / 5 + 32, round_to)


def fahrenheit_to_celsius(f, round_to=1):
    """Convert degrees Fahrenheit to degrees Celsius."""
    return round((f - 32) * 5 / 9, round_to)


print("\n  °C  |   °F")
print("------+-------")
for c in range(0, 101, 20):
    print(f"{c:5} | {celsius_to_fahrenheit(c):6}")

print("98.6 °F =", fahrenheit_to_celsius(98.6), "°C")
print("Round trip 37 °C:", fahrenheit_to_celsius(celsius_to_fahrenheit(37)))