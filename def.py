"""     Практичне завдання 1
Створи функцію def, яка знаходить квадрат числа. """
     
     
number = int(input("Enter  number: "))

def square(number):
    return number ** 2

print(square(number))






     
     
"""     Практичне завдання 2
Створи функцію, яка перевіряє, чи число парне. """


number = int(input("Enter number: "))

def is_even(number):
    return number % 2 == 0

if is_even(number) == True:
    print("Парне")
else:
    print("Не парне")



  
