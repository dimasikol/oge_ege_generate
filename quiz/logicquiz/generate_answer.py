import os
import json
import random
from apps.settings import BASE_DIR

with open(os.path.join(BASE_DIR, r'quiz/logicquiz/scratch_1.json'), 'r', encoding='UTF-8') as file:
    date_json = json.load(file)


def choice_variant(date, variant):  # обработка списка
    match variant:
        case "минимальное число":
            return (date, min(date))
        case "среднее число":
            if len(date) % 2 == 0:
                date.append(date[-1] + random.randint(1, 10))
            return (date, date[len(date) // 2])
        case "максимальное число":
            return (date, max(date))
        case "сумму":
            return (date, sum(date))
        case "среднее арифметическое чисел":
            return (date, sum(date) / len(date))
        case "простое число":
            simple_list = [i for i in date if i in date_json['easy_num']]
            if not (simple_list):
                simple_list = random.choice(date_json['easy_num'])
                date.append(simple_list)
            return (date, simple_list)
        case "кратное":
            chethost = random.randint(3, 17)
            return change(date, chethost) + (chethost,)
        case "четное число":
            return change(date, 2)
        case "не четное число":
            return change(date, 2, 1)
        case "количество чисел":
            date2 = ''.join(list(map(str, date)))
            num = str(random.randint(0, 9))
            num = num if num in date2 else date2[random.randint(0, len(date2) - 1)]
            return (date, date2.count(num), num + ' в 10 системе счисления')
        case "уникальное число":
            shufle = random.randint(1, 2)
            date2 = date[:shufle]
            date2.extend(date[:shufle])
            date2.append(date[-1])
            return (date2, date[-1])
        case "число, с суммой чисел в 10 системе счисления равной":
            date_sum = list(map(lambda x: sum(map(int, list(str(x)))), date))
            for i in date_sum:
                if date_sum.count(i) == 1:
                    num = i
                    break
            else:
                date[-1] = int(str(date[-1]) + '98')
                num = date_sum[-1] + 9 + 8
            return (date, num)

def change(date, chetnost, nechet=0):
    """
    :param date: #
    :param chetnost: # система счисления
    :param nechet:  # небоходимо для нечетных цифр в chetnost =2 а nechet = 1 и тогда будет все четные числа и одно нечетное
    :return: #date список с одним подходящим элементом
    """
    filter_list = list(filter(lambda x: x % chetnost == (0 + nechet), date))
    if not (filter_list):
        answer_index = random.randint(0, len(date) - 1)
        date[answer_index] += chetnost - (date[answer_index] % chetnost)
    elif len(filter_list) == 1:
        return (date, filter_list)
    else:
        date = [i + 1 if i % chetnost == (0 + nechet) else i for i in date]
        answer_index = random.randint(0, len(date) - 1)
        date[answer_index] += chetnost - (date[answer_index] % chetnost)
    if nechet == 1:
        date[answer_index] -= 1
    return (date, date[answer_index])

def int_or_null(num):
    if isinstance(num,list):
        num=num[0]
    if str(num).isdigit():
        return int(num)
    else:
        return 0