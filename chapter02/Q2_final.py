import random

while True:
    alphabet = [chr(ord("a") + i) for i in range(26)]
    rd = random.choice(alphabet)
    print(rd)

    if rd == "t":
        print("tが出ました")
        break
