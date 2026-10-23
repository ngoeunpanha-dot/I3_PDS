def digit_sum(n):
  total = 0
  temp = abs(n)
  while temp > 0:
    total += temp % 10
    temp //= 10
  return total


def reverse_number(n):
  rev = 0
  temp = abs(n)
  while temp > 0:
    rev = rev * 10 + (temp % 10)
    temp //= 10
  return rev * (-1 if n < 0 else 1)


def is_palindrome(n):
  if n < 0:
    return False
  return n == reverse_number(n)


# (a) Test the three functions
for num in [2026, 12321, 9875]:
  print(
      f"{num}: digit sum = {digit_sum(num)}, reversed ="
      f" {reverse_number(num)}, palindrome = {is_palindrome(num)}"
  )

# (b) Count how many palindrom
palindrome_count = sum(1 for i in range(10, 1000) if is_palindrome(i))
print(f"Palindromes from 10 to 999: {palindrome_count}\n")