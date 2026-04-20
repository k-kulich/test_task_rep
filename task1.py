def is_isomorphic(s: str, t: str) -> bool:
    """
    Проверка изоморфности 2 строк за O(n) по времени и O(k) по памяти, если n - длина строк,
    k - число уникальных символов (в худшем случае память O(n), если все символы уникальные).
    """
    if len(s) != len(t):
        return False
    map_s_to_t = {}
    map_t_to_s = {}
    for cs, ct in zip(s, t):
        if ct != map_s_to_t.get(cs, ct):  # O(1) тк словарь на основе хэш-таблицы
            return False
        else:
            map_s_to_t[cs] = ct
        
        if cs != map_t_to_s.get(ct, cs):  # O(1)
            return False
        else:
            map_t_to_s[ct] = cs
    return True

# пример из условия
s = 'paper'
t = 'title'
print(is_isomorphic(s, t))  # True

# пример неизоморфности
s = 'latte'
t = 'capuc'
print(is_isomorphic(s, t))  # False
