def eat_cookie(presents_left, nice_kids):  # създаваме фунцкия, първи параметър останалите подаръци и втори добрите деца
    for coordinates in directions.values():  # обхождаме всяка посока от посоките
        r = santa_pos[0] + coordinates[0]  # намираме реда като съберем реда на Дядо Коледа и реда от посоката
        c = santa_pos[1] + coordinates[1]  # намираме колоната като съберем колоната на Дядо Коледа и тази от посоката

        if neighborhood[r][c].isalpha():  # проверяваме дали сме стъпили на буква
            if neighborhood[r][c] == 'V':  # проверяваме дали сме в къщата на добро дете
                nice_kids += 1  # увеличаваме броя на посетените добри деца за скоупа на функцията

            neighborhood[r][c] = '-'  # заменяме позицията, на която сме с тире
            presents_left -= 1  # намаляме наличните подаръци с 1, в скоупа на функцията

        if not presents_left:  # проверяваме дали са ни свършили подаръците
            break  # прекратяваме цикъла

    return presents_left, nice_kids  # връщаме наличните подаръци и броя на посетените добри деца


presents = int(input())  # прочитаме броя подаръци
size = int(input())  # прочитаме размера на матрицата

neighborhood = []  # създаваме променлива, в която да пазим матрицата
santa_pos = []  # създаваме променлива, в която да пазим позицията на Дядо Коледа

total_nice_kids = 0  # създаваме променлива, в която да пазим броя на добрите деца
nice_kids_visited = 0  # създаваме променлива, в която да пазим броя на посетените добри деца

directions = {  # създаваме променлива, в която да пазим посоките
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):  # развъртаме цикъл за всеки ред, за да прочетем матрицата
    line = input().split()  # прочитаме ред от конзолата и го разделяме по спейс

    neighborhood.append(line)  # добавяме реда към матрицата

    if 'S' in line:  # проверяваме дали Дядо Коледа е на този ред
        santa_pos = [row, line.index('S')]  # запазваме позицията на Дядо Коледа
        neighborhood[row][santa_pos[1]] = '-'  # променяме стойността на позицията на Дядо Коледа на тире

    total_nice_kids += line.count('V')  # добавяме броя им от реда, към общия брой добри деца

command = input()  # прочитаме команда, опции - up, down, left, right, Christmas morning

while command != "Christmas morning":  # развъртаме while цикъл, докато командата е различна от Christmas morning
    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1],
    ]  # обновяваме позицията на Дядо Коледа, като събираме текущата му позиция с тази от координатите

    house = neighborhood[santa_pos[0]][santa_pos[1]]  # запазваме стойността на текущата къща

    if house == 'V':  # проверяваме дали в къщата има добро дете
        nice_kids_visited += 1  # увеличаваме броя на посетените добри деца
        presents -= 1  # намаляме броя на подаръците
    elif house == 'C':  # проверяваме дали в къщата има бисквитки
        presents, nice_kids_visited = eat_cookie(presents, nice_kids_visited)  # извикваме функцията eat_cookies()

    neighborhood[santa_pos[0]][santa_pos[1]] = '-'  # заменяме позицията, на която сме с тире

    if not presents or nice_kids_visited == total_nice_kids:
        break  # проверяваме дали са ни свършили подаръците или сме минали през всички добри деца в квартала

    command = input()  # прочитаме команда

neighborhood[santa_pos[0]][santa_pos[1]] = 'S'  # поставяме Дядо Коледа на позицията му

if not presents and nice_kids_visited < total_nice_kids:  # проверка нямаме подаръци и не сме посетили всички добри деца
    print('Santa ran out of presents!')  # принтираме, Santa ran out of presents!

print(*[' '.join(line) for line in neighborhood], sep='\n')  # принтираме матрицата, като джойнваме всеки ред по спейс

if total_nice_kids == nice_kids_visited:  # проверяваме дали всички добри деца са получили подаръци
    print(f'Good job, Santa! {nice_kids_visited} happy nice kid/s.')  # принтираме
else:  # ако не всички добри деца са получили подаръци
    print(f'No presents for {total_nice_kids - nice_kids_visited} nice kid/s.')  # принтираме
