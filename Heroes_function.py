#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Файл содержит функцию, которая описывает в общем виде следующую задачу. Надо вывести данные о всех героях,
# описанных на сайте (их пол и наличие / отсутствие работы), отфильтровать их в зависимости от значений указанных
# характеристик и вывести данные о самом высоком герое среди результатов фильтрации.
import requests
# Функция принимает на вход значение пола в формате строки, а также булеов значение, кодирующее наличие / отсутствие работы.
def the_highest_superhero(gender: str, has_job: bool):
# Считываем данные о всех героях в формате многоуровневого списка json.
   URL = "https://github.com/akabab/superhero-api/blob/master/api/all.json"
   response = requests.get(URL)
   superheroes = response.json()
# Выводим результаты фильтрации с помошью генератора списков.
   filtered_heroes = [
        hero for hero in superheroes
       # Функция проверяет, заполнено ли значение поля "occupation", и присваивает переменной has_job результат данной проверки (True / False).
        if hero["appearance"]["gender"] == gender and (has_job == (hero["work"]["occupation"] != '-'))
    ]
# Если по результатам поиска не удалось найти ни одной записи, функция выводит сообщение None.
   if not filtered_heroes:
    return None
# Находим среди отфильтрованных записей героя с максимальным ростом с помощью лямбда-выражения.
# Для удобства восприятия выведем только рост в сантиметрах.
   highest_hero = max(filtered_heroes, key=lambda x: x["appearance"]["height"][1])  # спользуем индекс [1] для получения роста в сантиметрах
   return highest_hero


# In[ ]:





# In[ ]:




