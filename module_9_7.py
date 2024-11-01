# Декораторы

def is_prime(func):
    def wrapper(*args):
        count, n = 0, func(*args)
        for i in range(2, n):
            if n % i == 0:
                count += 1
        if count > 0:
            print('Составное')
        else:
            print('Простое')
        return n            # func(*args)
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)
