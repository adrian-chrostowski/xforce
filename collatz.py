print("This is The Collatz Sequence")
user = int(input("Enter a number: "))


def collatz(n):
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            yield(n)
        else:
            n = n * 3 + 1
            yield(n)


print(list(collatz(user)))

