# Задание 3 (Вариант 13)

Разработать инструмент командной строки для учебного конфигурационного
языка, синтаксис которого приведен далее. Этот инструмент преобразует текст из
входного формата в выходной. Синтаксические ошибки выявляются с выдачей
сообщений.
Входной текст на языке xml принимается из стандартного ввода. Выходной
текст на учебном конфигурационном языке попадает в файл, путь к которому
задан ключом командной строки.

Многострочные комментарии:

{#
Это многострочный
комментарий
#}


Массивы:

({ значение, значение, значение, ... })

Словари:

dict(
имя = значение,
имя = значение,
имя = значение,
...
)

Имена:

[_A-Z][_a-zA-Z0-9]*


Значения:

• Числа.

• Массивы.

• Словари.

Объявление константы на этапе трансляции:

имя <- значение

Вычисление константного выражения на этапе трансляции (инфиксная
форма), пример:

[имя + 1]

Результатом вычисления константного выражения является значение.

Для константных вычислений определены операции и функции:

1. Сложение.

2. Вычитание.

3. Умножение.

4. sqrt().

5. len().

Все конструкции учебного конфигурационного языка (с учетом их
возможной вложенности) должны быть покрыты тестами. Необходимо показать 2
примера описания конфигураций из разных предметных областей.


# Решение
# Запуск для примера 1
```python3 tool.py input/example.xml output/result.txt```

# Результат для примера 1
<img width="928" alt="Снимок экрана 2024-12-17 в 7 00 43 PM" src="https://github.com/user-attachments/assets/7209b589-85dd-4c22-9b07-66de5dd9197c" />

# Запуск для примера 2

```python3 tool.py input/web_example.xml output/result.txt```

# Результат для примера 2
<img width="928" alt="Снимок экрана 2024-12-17 в 6 59 59 PM" src="https://github.com/user-attachments/assets/fcfe479c-c493-4fcb-9856-883a2f101481" />


# Тестирование
<img width="1073" alt="image" src="https://github.com/user-attachments/assets/07a9d2f9-354c-4b27-b677-9cdd4614b887" />







