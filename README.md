# Kursovaya_CL
 Курсовой проект по компьютерной лингвистике студентов группы ИВТ-365 Линцова И. и Щербинина В.

# Парсинг сайта и реализация web-интерфейса



# Модуль анализа новостей из БД
Выделить с помощью Томита-парсера упоминание в тексте значимых персон Волгоградской области и
достопримечательностей, также зафиксировать в БД записи с упоминаниями. Создать модуль для 
проведения с помощью Spark MlLib анализ модели word2vec на статьях из БД. Определить контекстные
синонимы и слова, с которыми они упоминались в тексте.

Персоны https://global-volgograd.ru/person 
Достопримечательности https://avolgograd.com/sights?obl=vgg

Для работы с Томитой был написан скрипт, алгоритм работы которого приведен ниже:
1. Подключиться к базе данных
2. Получить новости из базы данных по полям
3. Записать все новости в txt файл
4. Открыть файл на чтение и найти по названию факта результат
5. Записать найденный факт в массив персон/достопримечательностей
6. Записать в БД значения из массива персон и достопримечательностей

![photo_2022-01-06_02-43-22](https://user-images.githubusercontent.com/84631618/148478607-93808202-6f15-428c-89a3-bb1482bb6a9d.jpg)
![photo_2022-01-06_02-58-01](https://user-images.githubusercontent.com/84631618/148478612-bb1f4677-7f84-48b5-bf14-78813d48ad7c.jpg)
![photo_2022-01-06_04-23-56](https://user-images.githubusercontent.com/84631618/148478618-bbb96123-28db-4256-ba56-3e3296f4ccb5.jpg)
![image](https://user-images.githubusercontent.com/84631618/148478676-90826ab4-7ac7-45ec-9255-8ed8d1d3c239.png)




