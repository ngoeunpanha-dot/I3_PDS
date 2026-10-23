def is_leap(year):
  return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
def days_in_month(month, year):
  if month < 1 or month > 12:
    return None
  if month in (4, 6, 9, 11):
    return 30
  elif month == 2:
    return 29 if is_leap(year) else 28
  else:
    return 31
for y in [1900, 2000, 2024, 2026]:
  status = "" if is_leap(y) else "not "
  print(f"{y} {status}leap")

print(
    f"Feb 2024: {days_in_month(2, 2024)} | Feb 2026: {days_in_month(2, 2026)} |"
    f" Apr: {days_in_month(4, 2024)} | month 13: {days_in_month(13, 2024)}"
)
leap_count = sum(1 for y in range(2000, 2101) if is_leap(y))
print(f"Leap years from 2000 to 2100: {leap_count}\n")