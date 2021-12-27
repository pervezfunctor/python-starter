def factorial(n: int) -> int:
    assert n >= 0

    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


if __name__ == "__main__":
    print("hello world")
