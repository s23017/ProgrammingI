w = "○ "
b = "● "

for i in range(4):
    result = b * i + w + b * (3 - i)
    print(result)
