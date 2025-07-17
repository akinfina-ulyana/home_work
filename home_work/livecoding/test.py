# task 2
def func1(some_dict: dict):
    result = []
    for key, value in some_dict.items():
        if isinstance(value, dict):
            result.extend(func1(value))
        else:
            result.append((key, value))
    return result


# task 3
def get_value_by_key(data, key_path):
    keys = key_path.split(".")
    item = data
    for key in keys:
        if isinstance(item, dict) and key in item:
            item = item[key]
        else:
            return None
    return item


# task 6
def read_matrix_from_file(filename: str):
    with open(filename, "r", encoding="utf-8") as file:
        n = int(file.readline().strip())

        matrix = []
        for _ in range(n):
            row = list(map(int, file.readline().strip().split()))
            matrix.append(row)

    main_diag = sum(matrix[i][i] for i in range(n))
    secondary_diag = sum(matrix[i][n - i - 1] for i in range(n))

    result = abs(main_diag - secondary_diag)
    return result


# task 7
# Pallindrom

def palindrom_chek(some_str):
    clean_str = ''.join(char for char in some_str if char.isalpha() or char.isdigit())
    bool_res = True if clean_str == clean_str[::-1] else False
    return bool_res


print(palindrom_chek("1ffggh.25hggff1"))
print(palindrom_chek("1f,fgg.h2h:;ggff1"))


# task 8
def two_sum(num, target):
    num_dict = {}

    for index, number in enumerate(num):
        complement = target - number
        if complement in num_dict:
            return [num_dict[complement], index]
        num_dict[number] = index

    return []


nums = [3, 12, 2, 7, 8, 3, 4]
target = 15
result = two_sum(nums, target)
print(result)


# task 9
def uniq_obj_in_subsequence(nums_sub):
    res = list(dict.fromkeys(nums_sub))
    return len(res)


print(uniq_obj_in_subsequence([3, 5, 2, 6, 7, 8, 4, 2]))


def uniq_obj(sub):
    res = []
    for i in sub:
        if i not in res:
            res.append(i)
    return len(res)


# 10 retry
from typing import Callable


def retry(limit: int):
    def wrapper(func: Callable):
        count = 0

        def inner(*args, **kwargs):
            nonlocal count, limit
            if count < limit:
                func(*args, **kwargs)
                count += 1
            else:
                print('limit stop you')

        return inner

    return wrapper


@retry(2)
def my_fun(text):
    print(text)


res = my_fun('hello')

# task 11
import time
import asyncio
from contextlib import suppress


class AsyncTimer:
    def __init__(self):
        self.start_time = None

    async def __aenter__(self):
        self.start_time = time.perf_counter()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.perf_counter() - self.start_time
        if exc_type is not None:
            print(f"An error occurred: {exc_val}")
            with suppress(asyncio.CancelledError):
                pass
        print(f"Elapsed time: {elapsed_time:.4f} seconds")


# task 12
# Ошибку, так как изменяемый объект не может быть ключом в словаре

# 13
request_data = """
    2025-05-21T17:11:10 Вход в систему
    2025-05-21T17:11:12 Авторизация
    2025-05-21T17:11:25 Заполнение формы
    2025-05-21T17:15:14 Выход из системы
    """
from datetime import datetime


def average_time_between_events(data: str) -> float:
    lines = data.split('\n')
    timestamps = []
    for line in lines:
        clear_line = line.strip()
        timestamp_str = clear_line.split(' ')[0]
        timestamp = datetime.fromisoformat(timestamp_str)
        timestamps.append(timestamp)

    time_differences = []
    for i in range(1, len(timestamps)):
        difference = (timestamps[i] - timestamps[i - 1]).total_seconds()
        time_differences.append(difference)

    if time_differences:
        average = sum(time_differences) / len(time_differences)
    else:
        average = 0.0

    return average



# task 16
def own_zip(subsequence1, subsequence2):
    res = []
    min_seq = subsequence1 if subsequence1 <= subsequence2 else subsequence2
    for i in range(len(min_seq)):
        res.append([subsequence1[i], subsequence2[i]])
    return res


s = [1, 2, 3, 4, 5, 7]
s2 = [6, 7, 8, 9, 10, 7, 77]

print(own_zip(s, s2))
