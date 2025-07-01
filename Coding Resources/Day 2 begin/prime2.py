def get_primes(start_num, end_num):
    for num in range(start_num, end_num + 1):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num)

if __name__ == "__main__":
    get_primes(1, 100)