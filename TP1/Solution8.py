def describe(*numbers, decimals=2, label="Data"):
  if not numbers:
    print(f"{label}: no values")
    return None
  count = len(numbers)
  mn = min(numbers)
  mx = max(numbers)
  mean = round(sum(numbers) / count, decimals)
  print(f"{label}: n={count} min={mn} max={mx} mean={mean}")
  return numbers


def make_tag(text, **style):
  style_str = "".join(f' {k.replace("_", "-")}="{v}"' for k, v in style.items())
  return f"<span{style_str}>{text}</span>"


# (c) Lambdas
square = lambda x: x**2
is_adult = lambda age: age >= 18

# Tests
describe(12, 7, 30, 4)
describe(3.14159, 2.71828, decimals=3, label="Constants")
describe()
print(make_tag("Hello", color="red", size=14))
print(square(9), is_adult(17), is_adult(21))
print()