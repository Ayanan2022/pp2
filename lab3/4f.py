def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]


input_list = input("input: ").split()
input_list = [int(x) for x in input_list]
primes = filter_prime(input_list)
print("Prime numbers:", primes)
