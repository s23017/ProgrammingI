def print_multiplication_table():
    for i in range(1, 10):
        for j in range(1, 12):
            result = i * j
            print(f"{result:3}", end=" ")
        print()


if __name__ == "__main__":
    print_multiplication_table()
