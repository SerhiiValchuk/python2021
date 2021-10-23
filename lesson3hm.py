# написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи
#
# запишите 5 тудушек
# и выведете все
# 2) протипизировать первое задание

from typing import Callable, Union

Value = Union[Callable[[str], None], Callable[[], list[str]]]


def notebook() -> dict[str, Value]:
    todo_list: list[str] = []

    def get_all() -> list[str]:
        nonlocal todo_list
        return todo_list

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    return {
        "get_all": get_all,
        "add_todo": add_todo
    }


notebook1 = notebook()
notebook1['add_todo']("first")
notebook1['add_todo']("second")
print(notebook1.get('get_all')())

notebook2 = notebook()
notebook2['add_todo']("first2")
notebook2['add_todo']("second2")
print(notebook2.get('get_all')())


# 3) С помощью lambda функции извлеките из списка числа, делимые на 15 без остатка.


l = [15, 25, 30, 35, 78, 90, 165]


print(list(filter(lambda x: x % 15 == 0, l)))

# 4) написать функцию которая будет принимать целое число n и посчитайте n + nn + nnn.
# Пример:
# summ(7) -> 7+77+777=861

def summ(n: int) -> int:
    return sum(int(str(n) * i) for i in range(1, 4))


print(summ(8))