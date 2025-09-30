n = int(input())
arr = list(map(int, input().split()))
zeroes = 0
positives = 0
negatives = 0
for n in a:
  if n == 0:
    zeroes += 1
  elif n > 0:
    positives += 1
  else:
    negatives += 1
print(zeroes, positives, negatives)
           
