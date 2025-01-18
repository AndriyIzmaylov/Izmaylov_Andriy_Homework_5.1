# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
# Змінна не може:
# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної повинно складатись не більш чим з одного нижнього підкреслення "_".
# Список зареєстрованих слів можна взяти із keyword.kwlist.#
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.
# Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно :))
# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True

import re
import keyword


def variable_check(variable_name):
    pattern = r'^(?!__+$)(?!\d)(?!.*[A-Z])(?!.*[^a-z0-9_])(__[a-z]|[a-z_])[a-z0-9_]*$'
    if re.match(pattern, variable_name) and variable_name not in keyword.kwlist:
        return True
    return False


test_names = [
    "__name",
    " ",
    "_",
    "__",
    "___",
    "x",
    "get_value",
    "get value",
    "get!value",
    "some_super_puper_value",
    "Get_value",
    "get_Value",
    "getValue",
    "3m",
    "m3",
    "assert",
    "assert_exception"
]

for test_name in test_names:
    print(f"{test_name}: {variable_check(test_name)}")

print("*" * 60)
print("Now you can enter the variable to test")
print("*" * 60)
user_input = input("Enter the name of the variable: ")

print(f"{user_input}: {variable_check(user_input)}")
