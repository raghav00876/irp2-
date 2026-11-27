
n, k = map(int, input().split())
arr = list(map(int, input().split()))

seen = {}
count = 0

for num in arr:
    complement = k - num

    if complement in seen:
        count += seen[complement]

    seen[num] = seen.get(num, 0) + 1

print(count)
