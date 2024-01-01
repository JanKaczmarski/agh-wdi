# Largest Prime Factor

def main(n):
    i = 2
    while n > 1:
        while n % i == 0:
            n //= i
        i += 1
    return i - 1

print(main(600851475143))
