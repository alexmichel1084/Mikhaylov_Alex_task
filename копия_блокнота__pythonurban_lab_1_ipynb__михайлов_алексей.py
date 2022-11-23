# -*- coding: utf-8 -*-
"""Копия блокнота "PythonUrban_lab_1.ipynb" Михайлов Алексей

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qyqEm-tCTjob9WZYLfpsrS_illgvHCZA

## list comprehension

### Обработка каждого элемента
"""

cart = [3, 4, 12, 17, 19, 21, 23, 26, 30]

cashier = []  # новый список с помощью метода append
for item in cart:
    cashier.append(item)
print(cashier)

cashier = [item for item in cart]
print(cashier)

"""![](https://github.com/mrdbourke/python-list-comprehensions-tutorial/raw/f68f956c745932e1b824a69994706d715adde0a1/images/list-comprehensions-1.png)

### Фильтрация элементов
"""

cart = [5, 7, 9, 10, 12, 15, 19, 20, 22]

cashier_3 = []
for item in cart:
    if item % 2 == 0:  # только четные
        cashier_3.append(item)
print(cashier_3)

cashier_3 = [item for item in cart if item % 2 == 0]
print(cashier_3)

"""![](https://github.com/mrdbourke/python-list-comprehensions-tutorial/raw/f68f956c745932e1b824a69994706d715adde0a1/images/list-comprehensions-2.png)

## Задачи

##### ***Задача 1. Сделать название городов с заглавной буквы.***
Написать функцию task_1, которая будет принимать список названий городов, а возвращать новый список, в котором в каждой строке первая буква будет заглавной, а все остальные строчные.
"""

def task_1(list):
    new_list=[]
    #for item in list:
    #    new_list.append(item[0].upper()+item[1:len(item)].lower())
    new_list=[ (item[0].upper()+item[1:len(item)].lower()) for item in list ]
    return new_list

list_cities = ["москва", "иЖЕВСк", "Владивосток", "новосибирсК", "мУРМАНСК"]

...  # TODO написать функцию task_1

new_list_cities = task_1(list_cities)  # TODO вызвать функцию и получить новый результат исходного списка list_cities

print(new_list_cities)  # ['Москва', 'Ижевск', 'Владивосток', 'Новосибирск', 'Мурманск']

s="aaa"
print(s[0].upper())
print(s) # это я тут немножко экспериментировал

"""##### ***Задача 2. Отфильтровать города с населением больше 1 млн. человек.***

Написать функцию task_2, которая будет принимать два аргумента список городов и численность населения.  
Функция должна возвращать новый отфильтрованный список городов, где остались города только с население больше 1 млн. человек


"""

def task_2(list, filter_population) :
    new_list=[item for item in list if item['population'] > filter_population]
    return new_list

list_dict_cities = [
    {
        "name": "Москва",
        "population": 12 * 10 ** 6,
    },
    {
        "name": "Санкт-Петербург",
        "population": 5 * 10 ** 6,
    },
    {
        "name": "Ижевск",
        "population": 0.6 * 10 ** 6,
    },
]

filter_population = 10 ** 6

 # TODO написать функцию task_2

new_list_dict_cities = task_2(list_dict_cities, filter_population )  # TODO вызвать функцию и передать в неё значения list_dict_cities и filter_population

print(new_list_dict_cities)  # [{'name': 'Москва', 'population': 12000000}, {'name': 'Санкт-Петербург', 'population': 5000000}]

"""##### ***Задача 3. Найти общие города среди двух групп и отсортировать их в алфавитном порядке.***

Написать функцию task_3, которая будет принимать 2 списка городов, а возвращать новый список, в котором будут города, которые есть в двух группах.  
Результат функции должен быть отсортирован в алфавитном порядке. 

"""

def task_3(list, list2):
    return [n for n in list if n in list2]

fisrt_group = ["Москва", 'Владивосток', "Санкт-Петербург"]
second_group = ['Новосибирск', "Ижевск", "Санкт-Петербург", "Москва"]

...  # TODO Написать функцию task_3

common_cities = task_3(fisrt_group , second_group)  # TODO вызвать функцию и передать в неё значения fisrt_group и second_group

print(common_cities)  # ['Санкт-Петербург', 'Москва']

"""##### ***Задача 4. Найти количество упоминаний заданного города.***

У списка есть метод `count`, этот метод принимает значение,  
и считает сколько раз он содержится в списке.  

Написать функцию `task_4`, которая принимает два аргумента список городов,  
где нужно искать заданный город.  
И искомый город, количество упоминаний которого нужно подсчитать.
Результатом должно быть количество вхождений города в списке.

Города записанные в разных регистрах, считаются одинаковыми.
"""

def task_4(list,city):
    list = [item.lower() for item in list]
    return list.count(city.lower())

list_cities = [  # список городов
    'Новосибирск',
    'Владивосток',
    'Москва',
    'санкт-петербург',
    'Владивосток',
    'Москва',
    'Санкт-Петербург',
    'Москва',
    'Новосибирск',
    'Владивосток',
    'Ижевск',
    'Владивосток',
    'Ижевск',
    'САНКТ-ПЕТЕРБУРГ',
    'Владивосток',
    'Новосибирск',
    'Владивосток',
    'Ижевск',
    'Москва',
    'Санкт-Петербург'
]
find_city = 'Санкт-Петербург'  # искомый город

...  # написать функцию task_4

count_cities = task_4(list_cities, find_city)  # TODO вызвать функцию и передать в неё значения list_cities и find_city

print(count_cities)  # 4

"""##### ***Задача 5. Средний индекс озеленения.***

Дан список словарей территорий, где `territory_area` - площадь территории, а `green_zones` список площадей зеленых зон.  
Написать две функции:
- первая будет принимать исходный список городов, и возвращать новый список словарей, в котором для каждой территории посчитан индекс индекс озеленения, как отношение площади зеленых зон к площади территории. Новые словари в списке должен содержать название территории и её индекс озеленения. 
- вторая функция принимает список словарей, в которых посчитаны индексы озеленения для каждой территории и возвращает средний индекс озеленения по всем территориям. 
"""

def landscaping_index(list):
    dictionary={}
    for item in list:
        dictionary[item["territory_name"]] = sum(item["green_zones"]) / item["territory_area"] 
    return dictionary
def average_index(dict):
    average=0
    for item in dict:
        average+= dict[item]
    return average/3

list_territories = [
    {
        "territory_name": "Пушкин",
        "territory_area": 28676,
        "green_zones": [302, 487, 420, 325, 471, 363, 404]
    },
    {
        "territory_name": "Павловск",
        "territory_area": 21025,
        "green_zones": [360, 375, 223, 258, 345, 296, 303]
    },
    {
        "territory_name": "Петергоф",
        "territory_area": 44274,
        "green_zones": [364, 447, 438, 223, 336, 431, 442]
    },
]


# TODO написать функцию, которая будет высчитывать индексы озеленения для каждой территории

# TODO написать функцию, которая будет высчитывать средний индекс озеленения по всем территориям

# TODO распечатать результат округленный до 4 знаков после запятой

print(round(average_index(landscaping_index(list_territories)),4))