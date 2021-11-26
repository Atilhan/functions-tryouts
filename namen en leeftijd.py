def my_function():
    name = input ("What is your name ? ")
    age = int (input("What is your age ? "))
    print ( name , "Is" , age , "Years old")
    
my_function()

#--------------------- 2 verschillende manieren ---------------------#

def my_function(name,age):
    print (name , age)

my_function(input("What is yourname"),int(input("What is your age ?")))