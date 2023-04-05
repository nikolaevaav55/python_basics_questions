"""
 immutable : bool, int, float, string, tuple, frozenset, bytes
 mutable : list, dict, set, byte array

 https://habr.com/ru/companies/otus/articles/664302/ (Изменяемые и неизменяемые объекты в Python)
 https://habr.com/ru/articles/417783/ (Оптимизации, используемые в Python: список и кортеж)
"""

# immutable : int

x = 10
y = x

print(id(x) == id(y))  # True
print(id(y) == id(10))  # True

x = x + 1

print(id(x) != id(y))  # True
print(id(x) != id(10))  # True

# immutable : string

x = "some_string"
y = "some_string"

print(id(x))  # 2078008539376
print(id(y))  # 2078008539376
print(id(x) == id(y))  # True
print(x is y)  # True

# mutable : list

m = list([1, 2, 3])
n = m

id(m) == id(n)  # True
m.pop()

id(m) == id(n)  # True

# exceptions
my_tuple = ('string', [1, 2, 3])
print(id(my_tuple))  # 2470794654144
my_tuple[1].append(10)
print(my_tuple) # [1, 2, 3, 10]
print(id(my_tuple))  # 2470794654144


# objects to a function
# link to list
def update_list(my_list):
    my_list += [10]


n = [5, 6]
print(id(n))                  # 2822959142848
update_list(n)
print(n)                      # [5, 6, 10]
print(id(n))                  # 2822959142848


# passing by value
def update_number(n: int):
    """
    Когда функция вызывает значение, передается только значение переменной, а не сам объект.
    Таким образом, переменная, ссылающаяся на объект, не изменяется, а сам объект изменяется,
    но только в пределах области видимости функции. Следовательно, изменение не видно «снаружи»
    """
    n += 10
    print(id(n))


b = 5
print(id(b))  # 2409024782704
update_number(b)  # 2409024783024
print(b)  # 5
print(id(b))  # 2409024782704