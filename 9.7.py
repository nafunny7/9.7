def is_prime(func):
    def wrapper(*args):
        lol = func(*args)
        if lol > 1:
            for i in range(2, int(lol ** 0.5) + 1):
                if lol % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        return lol

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
