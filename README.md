# Python Advanced Notebook

---

## Helpful Links:

- [Big O Notations and Time Complexity](https://flexiple.com/algorithms/big-o-notation-cheat-sheet)

---

## Theoretical Tests:

- [Lists as Stacks and Queues](https://forms.gle/XP8QW5K59yMGQE7N8)


- [Tuples and Sets](https://forms.gle/AW52AwMsgNbvQfMf7)


- [Multidimensional Lists](https://forms.gle/h5rchwrtc4jaanzE6)


- [Functions](https://forms.gle/ZEXu7H1VAidyxMx19)


- [Error Handling](https://forms.gle/kz2vCqLuZ8MJhZvX6)


- [File Handling](https://forms.gle/kPob4JXS4pcF75J27)

---

## Notebook:

### 01. Lists as Stacks and Queues (Списъци като Стекове и Опашки)

1. Time Complexity
   - Броя операции при определен брой входни данни
   - Използваме го, за да измерваме бързодействието на един алгоритъм
   - Инструменти за измерване:
     - Big O notation - показва **worst case** сложност на алгоритъма
     - Big – Theta(Θ) notation - показва **average case** сложност на алгоритъма
     - Omega notation - показва **best case** сложност на алгоритъма
       
2. Stack - Стек
   - Линейна структура -> всеки елемент освен първия и последния, има предишен и следващ
   - **LIFO** order -> **L**ast element **I**n **F**irst element **O**ut
   - Типично се реализира с **Linked List**(Свързан списък)
   - В Python можем да използваме списък, за да постигнем подобен ефект, благодарение на методите **append**, **pop**
3. Queue - Опашка
   - Линейна структура
   - Може да бъде реализирана, както с **Linked List**, така и с **Double Linked List**
   - В Python queue е реализиран с **Double Linked List**
   - **FIFO** order -> **F**isrt element **I**n **F**irst element **O**ut

---

### 02. Tuples and Sets (Кортежи и множества)

1. Tuples (Кортежи)
   - Read-Only collection
   - Immutable (не могат да бъдат променяни)
   - Синтаксис:
     ```py
     tuple1 = (1, )
     tuple2 = (1, 2, 3)
     ```

2. Sets (Множества)
  - Неподредена колекция
  - Пази само уникални стойности
  - Изобразяват се чрез Вен диаграми
  - Операции върху множества:
    - intersection (сечение) - A ∩ B - всички общи елементи от А и В
      </br>
      <img height=150 width=300 src="https://cdn1.byjus.com/wp-content/uploads/2021/05/Venn-diagrams-6.png">
    - union (обединение) - А U В - всички елементи от А и В
      </br>
      <img height=150 width=300 src="https://cdn1.byjus.com/wp-content/uploads/2021/05/Venn-diagrams-7.png">
    - difference (разлика) - А - В - всички различни елементи в А, които не присъстват в В
      </br>
      <img height=150 width=300 src="https://cdn1.byjus.com/wp-content/uploads/2021/07/difference-of-a-and-b.png">
    - symmetrical difference (симетрична разлика) - A ^ B - всички различни елементи от А, които не присъстват в В и всички елементи от В, които не присъстват в А.
      </br>
      <img height=150 width=300 src="https://cdn1.byjus.com/wp-content/uploads/2021/07/symmetric-difference-between-a-and-b.png">
  - Синтаксис:
       ```py
       my_set_1 = {1, 2, 3, 4}
       my_set_2 = {3, 4, 5, 6}
   
       print(my_set_1.intersection(my_set_2))  # {3, 4}
       print(my_set_1.union(my_set_2))  # {1, 2, 3, 4, 5, 6}
       print(my_set_1.difference(my_set_2))  # {1, 2}
       print(my_set_2.difference(my_set_1))  # {5, 6}
       print(my_set_1.symmetric_difference(my_set_2)) # {1, 2, 5, 6}
       print(my_set_2.symmetric_difference(my_set_1)) # {1, 2, 5, 6}
       ```
---

### 03. Multidimensional Lists (Многомерни Списъци)

   1. Какво представляват многомерните списъци?
      - Списък от списъци
        ```py
        matrix = [
           [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
        ]
        ```
   2. Как достъпваме даниите в многомерен списък?
      ```py
         print(matrix[0][0]  # 1
         print(matrix[1][1]  # 5
         print(matrix[2][0]  # 7
      ```
      - Казвайки `matrix[0]`, достъпваме списъка на първа позиция, т.е. `[1, 2, 3]`
      - Казвайки `matrix[0][0]`, достъпваме елемента на индекс **0** в списъка намиращ се на индекс **0**, във външния списък. 

---

### 04. Functions Advanced

   1. Пакетиране на аргументи.
      - Понякога искаме функция да може да приема различен брой аргументи при всяко извикване.
      - Начина, по който постигаме това е чрез пакетиране
      ```py
      def find_average(*nums):  # подадените n на брой параметри ще бъдат пакетирани в списък с променлива на име nums
         # nums => [10, 11, 9, 7, -12, 56]
         return sum(nums) / len(nums)

      find_nums(10, 11, 9, 7, -12, 56)
      ```
      - Освен стандартни аргумети можем да пакетираме и key-word аргументи
      - За разлика от стандартните те биват запазени в речник
      ```py
      def print_people_data(**names):  # {ivan: 20, emily: 32, pesho: 16}
         for name, age in names.items():
            print(f"{name} is {age} years old")

      print_people_data(ivan=20, emily=32, pesho=16)
      ```
      - Ако искаме да подадем определен брой единични аргумети, то можем да го направим, стига да бъдат подадени като първи
      ```py
      def my_func(param1, param2, *args, **kwargs):
         # param1 => 1
         # param2 => hi
         # args => [32, 31]
         # kwargs => {name: pesho}
         pass

      my_func(1, "hi", 32, 31, name="pesho")
      ```

   2. Разопаковане
      - Освен да пакетираме аргументи, то можем и да ги вадим от този "пакет"
      ```py
      numbers = [1, 2, 3]
      print(*numbers) # => *numbers ще извади всяка стойност и ще я подаде като отделен аргумент => print(1, 2, 3)
      ```

   3. Анонимни функции
      - lambda(анонимните) функции използваме предимно за кратки изрази
      ```py
      lambda a, b: a + b

      # еквивалетна функция
      def sum(a, b)
         return a + b
      ```

   4. Вложени функции
      - Вложените функции ни позволяват да достъпваме променливи от scope-a над тях
      ```py
      def outer_func():
         a = 5

         def inner_func():
            print(a)

         inner_func()

      outer_func() # console => 5
      ```

   5. Recursion
      - Функция, която извика себе си, има дъно и пълни stack-a
      - Кога използваме рекурсия?
        - Когато искаме да използваме stack-a, който идва от машината
      - **Всеки рекурсивен проблем, може да бъде решен итеративно**
      ```py
      def fibonacci(n):
         if n <= 1:
            return n

         return fibonacci(n - 1) + fibonacci(n - 2)
      ```
---

### 05. Error Handling
   1. Грешки и Изключения (Errors and Exceptions)
      - Какво е грешка?
        - Проблем или дефект, който се появява в програмата, водейки до неочаквано поведение.
      - Какво е изключение?
        - Събитие, което се случва по време на изпълнение на програмата и нарушава нейното изпълнение

   2. Типове грешки:
      </br>
      <img src="https://chercher.tech/images/python-programming/python-exception-heirarchi.png" width="600" height="300">

   3. Обработване на грешки
      - С логическите блокове **try**, **except**, ние можем да улавяме грешки
      ```py
      def divide_numbers(x, y):
          try:
              result = x / y
          except ZeroDivisionError:  # catches the error, must be included
              print("Error: You can't divide by zero.")
          else:  # prints only in the case that we don't have an error, optional
              print(f"The result is {result}")
          finally:  # prints no matter the result from the try-except block, optional
              print("Execution of divide_numbers is complete.")
      ```

   4. Custom Exceptions
      - Създаваме клас, който задължително наследява **Exception**
      ```py
      class MyException(Exception):
         pass

      raise MyException  # извикваме грешката
      ```
---

### 06. File Handling

   1. Отваряне на файлове
      - Използваме функцията **open()**
      - Тя приема 2 параметъра
        - Абсолютен или относителен път до файл
        - Тип на отваряне на файла
          - **w** - отваря файла за писане, като презаписва предишните данни в него
          - **x** - създава нов файл и го отваря за писане, ако вече има файл, хвърля грешка
          - **a** - отваря файла за писане, но добавя към предишните данни, вместо да ги изтрива
          - **t** - отваря файла в текстове режим, за писане и четене
          - **b** - binary mode
          - **+** - добавя четене или писане към съответния режим. Пример: **rw+**

   2. FileNotFoundError
      ```py
         try:
            text_file = open('text.txt', 'r')
            print("File found")
         except FileNotFoundError:
            print("File not found")
      ```

   3. Методи
      - readline - прочита n на брой символа
      ```py
         file = open("text.txt") # 'Hello, SoftUni!'
         print(file.readline(5)) # 'Hello
      ```
      - readlines - прочита всички редове и връща списък
      ```py
         file = open("text.txt")
         print(file.readlines())
         # ['Every\n', 'Word\n', 'is\n', 'line']
      ```
      - close - затваря файла - **опитваме се да не забравяме затварянето на отворени файлове**
      ```py
      file = open('python.txt', 'w')
      # Creates or opens the file
      file.write("This is the write command.\n")
      file.write("It allows us to write in a particular file")
      file.close()
      ```

   4. With statement
      - Отваря файла и когато излезем от блока, го затваря автоматично
      ```py
         with open("file.txt", "w") as f:
            f.write("Hello World!!!")
      ```

   5. Изтриване на файл
      ```py
         import os
         os.remove("python.txt")
         os.remove("D:\\text.txt")
      ```

---
