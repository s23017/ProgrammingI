N = int(input())
d = []

for _ in range(N):
    num = int(input())
    d.append(num)

for i in range(N):
    for j in range(i + 1, N):
        if d[i] < d[j]:
            d[i], d[j] = d[j], d[i]

print(" ".join(map(str, d)))
