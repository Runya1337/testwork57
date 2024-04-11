def prime_numbers(min_num, max_num):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [n for n in range(min_num, max_num + 1) if is_prime(n)]

def eratosthenes(min_num, max_num): 
    sieve = [True] * (max_num + 1)
    primes = []
    for p in range(2, max_num + 1):
        if sieve[p]:
            if p >= min_num:
                primes.append(p)
            for i in range(p * p, max_num + 1, p):
                sieve[i] = False
    return primes

print(prime_numbers(10, 100))
print(eratosthenes(10, 100))
