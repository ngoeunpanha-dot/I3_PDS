def is_prime(n):
  if n < 2:
    return False
  d = 2
  while d * d <= n:
    if n % d == 0:
      return False
    d += 1
  return True


# (b) Print primes
print("Primes below 50:", end=" ")
for p in range(2, 50):
  if is_prime(p):
    print(p, end=" ")
print()

primes_below_100_count = sum(1 for p in range(2, 100) if is_prime(p))
print(f"Number of primes below 100: {primes_below_100_count}")


# (c) Goldbach function
def goldbach(n):
  for p in range(2, n):
    if is_prime(p):
      q = n - p
      if is_prime(q):
        return (p, q)
  return None


for ev in range(4, 32, 2):
  p, q = goldbach(ev)
  print(f"{ev} = {p} + {q}")

# (d) Loop
holds = True
for ev in range(4, 10001, 2):
  if goldbach(ev) is None:
    holds = False
    break

print(f"Goldbach holds for every even number from 4 to 10000: {holds}")