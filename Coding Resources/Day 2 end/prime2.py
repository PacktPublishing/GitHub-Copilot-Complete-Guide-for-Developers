def get_primes(start_num, end_num):
    with open("primes.txt", "w") as file:  # Open a file in write mode
        for num in range(start_num, end_num + 1):
            prime = True
            for i in range(2, num):
                if num % i == 0:
                    prime = False
                    break
            if prime and num > 1:  # Ensure the number is greater than 1
                print(num)
                file.write(f"{num}\n")  # Write the prime number to the file

if __name__ == "__main__":
    get_primes(1, 100)