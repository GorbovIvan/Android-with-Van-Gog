#print("Hello World!") #Вывести "Привет мир"
#input()  #Ввести текст

#print(list("Cool dude")) #лист задать
#list = {"android": "cool dude"} #задать словарь и вывести только первое слово
#print(list["android"])
#input() #задать иначе вылетит python console

#Первая игра на Python
import random
right_answer = random.randint(1, 100)
user_answer = None
processed_answer = None
while True:
    user_answer = input("Guess the number in diaposone 1 to 100!")
    try:
        processed_answer = int(user_answer)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if processed_answer == right_answer:
        print("You Win!")
        break
    elif processed_answer < right_answer:
        print("Too low! Try again.")
        continue
    elif processed_answer > right_answer:
        print("Too high! Try again.")
        continue
input()

