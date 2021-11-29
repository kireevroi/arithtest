import random
import operator
#importing random for randint
OPERATORS = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
}

def cool_text(text_string):
    text_len = 100
    print(text_string.center(80, '*'))

#Заглавный экран
cool_text("Введите сложность (количество цифр в числах)")
complexity = input()
#cool_text("Введите какие операторы будут использоваться (0: + , 1: - ,2: * )")
#operand_input = input()
cool_text("Нажмите Enter, чтобы начать, \"q\", чтобы выйти")
start = input()
if start == 'q':
    exit()
win_counter = 0
while(True):
    first_num = random.randint(0, 10**int(complexity))
    second_num = random.randint(0, 10**int(complexity))
    #operand = OPERATORS[operand_input]
    print(str(max(first_num, second_num))+"+"+str(min(first_num, second_num))+"=", end = '')
    in_put = input()
    if in_put.lower() == "q":
        print("Ты заработала "+str(win_counter)+" очков!!!!! Молодец!!!!")
        break
    if int(in_put) == first_num+second_num:
        print("Молодец")
        win_counter = win_counter + 1
    else:
        print("Ошибка!")
ex = input()
