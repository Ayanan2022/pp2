class PrimeFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def filter_primes(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))

    def get_input_and_filter(self):
        user_input = input(" ")
        self.numbers = list(map(int, user_input.split())) 
        prime_numbers = self.filter_primes()
        print("Prime numbers:", prime_numbers)

prime_filter = PrimeFilter([])
prime_filter.get_input_and_filter()
