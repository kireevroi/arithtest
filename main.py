import random
import operator
from lib import dbinteraction as db
#importing random for randint
OPERATORS = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
}

def cool_text(text_string):
    text_len = 100
    print(text_string.center(80, '*'))



#Initializing database
db.dbinit('db_stats')
#Main screen
#name input
cool_text("Как Вас зовут?")
name = input()
#complexity input
cool_text("Введите сложность (количество цифр в числах)")
complexity = input()
#cool_text("Введите какие операторы будут использоваться (0: + , 1: - ,2: * )")
#operand_input = input()
complexity = int(complexity)
#start
cool_text("Нажмите Enter, чтобы начать, \"q\", чтобы выйти")
start = input()
#exit case (should maybe move to another function)
if start == 'q':
    exit

#initializing variables
win_counter = 0

#calculation loop
while(True):

    #generating random numbers
    first_num = random.randint(0, 10**int(complexity))
    second_num = random.randint(0, 10**int(complexity))
    #operand = OPERATORS[operand_input]

    # returning the max + min = formula
    print(str(max(first_num, second_num))+"+"+str(min(first_num, second_num))+"=", end = '')
    in_put = input()
    #exit case
    if in_put.lower() == "q":
        db.dbappend('db_stats', name, win_counter)
        break
    #calculation case
    if int(in_put) == first_num+second_num:
        print("Молодец")
        win_counter = win_counter + 1*complexity
    #wrong answer case
    else:
        print("Ошибка!")

#returning statistics
cool_text("Победители")
db.dbprint('db_stats')

#waiting for exit
ex = input()
