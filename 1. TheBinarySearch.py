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

    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
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
