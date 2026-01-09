print("Start!!")

low = 1
high = 100
steps = 0

while True:
    steps += 1
    guess = (low + high) // 2

    print(f"Ваше число {guess}?")
    answer = input("Ваша відповідь: (б)ільше (м)енше (т)ак: ").lower()

    if answer == "т":
        print(f"Ваше число {guess} було вгадано за {steps} кроків!")
        break
    elif answer == "м":
        high = guess - 1
    elif answer == "б":
        low = guess + 1
