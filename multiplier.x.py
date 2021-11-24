multiply = int(input('\033[1;35;20m'+'What multiplication tables do you wanna see ? '))

def math (multiply:int):
    for m in range (1,11):
        answer = m * multiply
        print (+ m, 'x', multiply , '=', (answer))

math(multiply)

