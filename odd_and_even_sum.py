n = int(input())
arr = list(map(int, input().split()))
odd_sum = 0
even_sum = 0
for n in arr:
  if n%2 == 0:
    even_sum += n
  else:
    odd_sum += n
print(odd_sum, even_sum)
