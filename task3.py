def prime_factors(num: int) -> list:
    """
    Разложить число на простые множители за O(sqrt(n)) по времени и O(log_2 n) по памяти.
    Сложность по времени обусловлена обходом чисел до корня из n.
    Сложность по памяти обусловлена хранением делителей (их не больше log_2 n).
    """
    factors = []
    # 2 отдельно
    while num % 2 == 0:
        factors.append(2)
        num //= 2
    # нечетные множители
    d = 3
    while d * d <= num:
        while num % d == 0:
            factors.append(d)
            num //= d
        d += 2
    if num > 1:
        factors.append(num)
    return factors


# пример
n = 56
print(prime_factors(n))  # [2, 2, 2, 7]

# пример для простого числа
n = 73
print(prime_factors(n))  # [73]