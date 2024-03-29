"""Utility module for primes."""

from collections import Counter
import math

# Lazily calculated.
_primes = [2]

def prime_generator():
    """Generator for prime numbers.

    Yields:
        Prime numbers in incremental order calculated using the sieve of
        ertosthenes.
    """
    num_primes = 0
    while True:
        if num_primes < len(_primes):
            yield _primes[num_primes]
        else:
            num_primes += 1
            next_prime = _primes[-1]
            is_next_prime = False
            while not is_next_prime:
                if next_prime == 2:
                    next_prime = 3
                else:
                    next_prime += 2
                next_prime_sqrt = math.sqrt(next_prime)
                for p in _primes:
                    if p > math.floor(next_prime_sqrt):
                        is_next_prime = True
                        break
                    elif not next_prime % p:
                        # Not prime
                        break
            _primes.append(next_prime)
            yield next_prime
        num_primes += 1

# Maps a number to a list of prime factors
_prime_factor_cache = dict()

def prime_factors(n):
    """Finds prime factors of a given number.

    Args:
        n - Number to find prime factors for.

    Returns:
        List containing prime factors.
    """
    factors = list()
    if n == 1:
        return factors

    if n in _prime_factor_cache:
        return _prime_factor_cache[n]

    halfN = n << 1
    for p in prime_generator():
        if not n % p:
            factors.append(p)
            factors.extend(prime_factors(n / p))
            break

    _prime_factor_cache[n] = factors
    return factors

def num_divisors(n):
    """Finds the number of divisors of n.

    Args:
        n - Number to find number of divisors for.

    Returns:
        Number of divisors of n
    """
    factors = prime_factors(n)
    count_dict = Counter(factors)
    divisors = 1
    for k, count in count_dict.iteritems():
        divisors *= (count + 1)
    return divisors