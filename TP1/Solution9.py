def electricity_bill(kwh):
  if kwh < 0:
    return None
  t1 = min(max(kwh, 0), 50)
  t2 = min(max(kwh - 50, 0), 150)
  t3 = max(kwh - 200, 0)

  subtotal = t1 * 480 + t2 * 610 + t3 * 730
  total = (subtotal + 2000) * 1.1
  return round(total)


# (b) Print a table
for kwh in [0, 35, 50, 120, 200, 350]:
  bill = electricity_bill(kwh)
  usd = bill / 4100
  print(f"{kwh:>3} kWh -> {bill:>9,} riel  (= {usd:>6.2f} USD)")

# (c) Ask user for monthly consumption
try:
  user_kwh = float(
      input("\nEnter your monthly consumption in kWh (e.g., 120): ")
  )
  user_bill = electricity_bill(user_kwh)
  if user_bill is not None:
    print(
        f"Your bill: {user_bill:,} riel (= {user_bill / 4100:.2f} USD)"
    )
  else:
    print("Invalid consumption value.")
except ValueError:
  print("Please enter a valid numeric value.")

print()
