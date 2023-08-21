def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


num = int(input("自然数を入力してください: "))
if is_prime(num):
    print(f"{num} は素数です")
else:
    print(f"{num} は素数ではありません")
