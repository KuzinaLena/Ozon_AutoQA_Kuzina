#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Создадим unit-тесты, позволяющие проверить работу ранее созданной функции для всех возможных комбинаций входных данных.
import unittest
import requests


# In[22]:


# Считываем функцию из другого файла.
from Heroes_function import the_highest_superhero
# Создадим тестовый класс, который наследуется от класса unittest.TestCase.
class TestTheHighestSuperhero(unittest.TestCase):
# Класс содержит 6 вариантов функции поиска самого высокого героя, различающихся комбинацией значений входных данных.
# Каждый тест содержит методы проверки различных типов: результат поиска не является пустым; все найденные герои указанного пола; для всех из них
# заполнен / не заполнен пункт "occupation".
# 1. Герои мужского пола, имеющие работу:
   def the_highest_male_with_job(self):
      result = the_highest_superhero("Male", True)
      self.assertIsNotNone(result)
      self.assertEqual(result["appearance"]["gender"], "Male")
      self.assertNotEqual(result["work"]["occupation"], "-")

# 2. Герои женского пола, имеющие работу:
   def the_highest_female_with_job(self):
      result = the_highest_superhero("Female", True)
      self.assertIsNotNone(result)
      self.assertEqual(result["appearance"]["gender"], "Female")
      self.assertNotEqual(result["work"]["occupation"], "-")

# 3. Герои, имеющие работу, для которых не указано название пола:
   def the_highest_unknown_gender_with_job(self):
      result = the_highest_superhero("-", True)
      self.assertIsNotNone(result)
      self.assertEqual(result["appearance"]["gender"], "-")
      self.assertNotEqual(result["work"]["occupation"], "-")

# 4. Герои мужского пола, не имеющие работы:
   def the_highest_male_without_job(self):
      result = the_highest_superhero("Male", False)
      self.assertIsNotNone(result)
      self.assertEqual(result["appearance"]["gender"], "Male")
      self.assertEqual(result["work"]["occupation"], "-")

# 5. Герои женского пола, не имеющие работы:
   def the_highest_female_without_job(self):
      result = the_highest_superhero("Female", False)
      self.assertIsNotNone(result)
      self.assertEqual(result["appearance"]["gender"], "Female")
      self.assertEqual(result["work"]["occupation"], "-")

# 6. Герои, не имеющие работы, для которых не указано название пола:
   def the_highest_unknown_gender_without_job(self):
      result = the_highest_superhero("-", False)
      self.assertIsNotNone(result)
      self.assertEqual(result["appearance"]["gender"], "-")
      self.assertEqual(result["work"]["occupation"], "-")
       
if __name__ == "__main__":
    unittest.main()


# In[ ]:




