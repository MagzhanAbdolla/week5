a = [int(i) for i in input().split()]
maxDig = a[0]
maxIndex = 0
for i, x in enumerate(a):
    if x >= maxDig:
        maxIndex = i
        maxDig = x
print(maxDig, maxIndex)
