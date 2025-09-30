n = int(input())
alt = list(map(int, input().split()))
current_alt = 0
max_alt = 0
for change in alt:
  current_alt += change
  if current_alt > max_alt:
    max_alt = current_alt
print(max_alt)
