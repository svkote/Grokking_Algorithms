"""
Бинарный поиск на входе получает отсортированный список элементов.
Если элемент, который ищем, присутствует в списке, то бинарный поиск возвращает его позицию.
В противном случае вернёт null.

Бинарный поиск работает только в том случае, если список отсортирован.

Мы можем использовать 2 метода:
- рекурсивный
- итерационный
"""


# итерационный
def binary_search(lst, item):
    if len(lst) == 0:
        return False

    # В переменных first и last хранятся границы части списка, в которой происходит поиск
    first = 0
    last = len(lst) - 1

    found = False

    while first <= last and not found:  # Пока граница не сократится до одного элемента или не будет найден элемент
        midpoint = (first + last) // 2
        if lst[midpoint] == item:
            found = midpoint
        else:
            if item < lst[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


# рекурсивный
def binary_search_rec(lst, item):
    if len(lst) == 0:
        return False
    else:
        midpoint = len(lst) // 2
        if lst[midpoint] == item:
            return midpoint
        else:
            if item < lst[midpoint]:
                return binary_search_rec(lst[:midpoint], item)
            else:
                return binary_search_rec(lst[midpoint + 1:], item)


"""Сложность алгоритма  O(log2 n)"""

"""
Задачи.
1. Максимальное количество проверок для списка из 128 имен при бинарном методе поиска - 7 (2 ** 7 == 128)
2. Если список увеличится вдвое, то макс.кол-во проверок будет - 8
"""
