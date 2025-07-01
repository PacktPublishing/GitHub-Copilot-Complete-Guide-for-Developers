def find_prime_in_range(start, end):
    prime_numbers = []
    a, b = 0, 1
    while b <= end:
        if b >= start:
            prime_numbers.append(b)
        a, b = b, a + b
    return prime_numbers

if __name__ == "__main__":
    prime_numbers = find_prime_in_range(1, 100)
    print("prime numbers between 1 and 100:", prime_numbers)
