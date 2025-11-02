# Vježba 14: Prosti brojevi

#     Napišite funkciju isPrime() koja prima cijeli broj i vraća True ako je broj prost, a False ako nije. Prost broj je prirodan broj veći od 1 koji je dijeljiv jedino s 1 i samim sobom.

# Primjer:

# print(isPrime(7)) # True
# print(isPrime(10)) # False

#     Napišite funkciju primes_in_range() koja prima dva argumenta: start i end i vraća listu svih prostih brojeva u tom rasponu.

# Primjer:

# print(primes_in_range(1, 10)) # [2, 3, 5, 7]


def isPrime(n: int) -> bool:
    """Return True if n is a prime number, else False."""
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False

    # check only 6k ± 1 candidates up to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


print(isPrime(7))  # True
print(isPrime(10))  # False


# manual walk, using the isPrime() function
def primes_in_range(start: int, stop: int) -> list[int]:
    result_list: list[int] = []
    for i in range(start, stop, 1):
        if isPrime(i):
            result_list.append(i)

    return result_list


print(primes_in_range(1, 10))
