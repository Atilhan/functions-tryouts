num_1 = 0
num_2 = 1

def fibonacci(num_1,num_2):
    outcome = num_1 + num_2
    return outcome

    
for math in range(8):
    num_x = (fibonacci(num_1,num_2))
    num_1 = num_2
    num_2 = num_x
    print(fibonacci(num_1,num_2))

