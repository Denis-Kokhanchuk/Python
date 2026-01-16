
"""       Практичне завдання: «Калькулятор IMC»
   Створіть програму, яка:Запитує ім'я (name), вагу (weight) та зріст (height).
   Рахує індекс за формулою: IMC = weight / height^2.
   Визначає норму (від 18.5 до 24.9) у вигляді True/False.
   Виводить повідомлення: "Користувач [ім'я], ваш IMC: [результат]. Норма: [True/False]". """


name = input("Enter your name: ")
weight = float(input("Enter your weight: "))
height_cm = float(input("Enter your height: "))

height = height_cm / 100
imc = weight / (height ** 2)

imc_norma = 18.5 <= imc <= 24.9

print(f"Користувач {name}, ваш IMC: {imc}. Норма: {imc_norma}.")


