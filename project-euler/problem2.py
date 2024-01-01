# Even Fibonacci Numbers

def main(cap=(4 * 10 ** 6 + 1)):
    suma = 0
    a, b = 1, 2
    while b < cap:
        if b % 2 == 0:
            suma += b
        a, b = b, a + b
    return suma


if __name__ == "__main__":
    print(main())