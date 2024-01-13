# Python Advanced Notebook

---

## Helpful Links:

- [Big O Notations and Time Complexity](https://flexiple.com/algorithms/big-o-notation-cheat-sheet)

---

## Theoretical Tests:

- [Lists as Stacks and Queues](https://forms.gle/XP8QW5K59yMGQE7N8)
- [Tuples and Sets](https://forms.gle/AW52AwMsgNbvQfMf7)

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

### Tuples and Sets (Кортежи и множества)

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
    - symmetrical difference (симетрична разлика) - всички различни елементи от А, които не присъстват в В и всички елементи от В, които не присъстват в А.
      </br>
      <img height=150 width=300 src="https://cdn1.byjus.com/wp-content/uploads/2021/07/symmetric-difference-between-a-and-b.png">
  - Синтаксис:
       ```py
       my_set_1 = {1, 2, 3, 4}
       my_set_2 = {3, 4, 5, 6}
   
       print(my_set_1.intersection(my_set_2))  # {3, 4}
       print(my_set_1.union(my_set_2))  # {1, 2, 3, 4, 5, 6}
       print(my_set_1.difference(my_set_2))  # {1, 2}
       print(my_set_2.difference(my_set_1))  # {3, 4}
       print(my_set_1.symmetric_difference(my_set_2)) # {1, 2, 5, 6}
       print(my_set_2.symmetric_difference(my_set_1)) # {1, 2, 5, 6}
       ```
---

