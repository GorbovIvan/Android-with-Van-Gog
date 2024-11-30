#print("Hello World!") #Вывести "Привет мир"
#input()  #Ввести текст

#print(list("Cool dude")) #лист задать
#list = {"android": "cool dude"} #задать словарь и вывести только первое слово
#print(list["android"])
#input() #задать иначе вылетит python console

#Первая игра на Python
#import random
#right_answer = random.randint(1, 100)
#user_answer = None
#processed_answer = None
#while True:
#    user_answer = input("Guess the number in diaposone 1 to 100!")
#   try:
#        processed_answer = int(user_answer)
#    except ValueError:
#        print("Invalid input. Please enter a number.")
#        continue
#    if processed_answer == right_answer:
#       print("You Win!")
#        break
#   elif processed_answer < right_answer:
#       print("Too low! Try again.")
#       continue
#       print("Too high! Try again.")
#       continue
#input()

def Addition(first, second):
    return first + second

def Subtraction(first, second):
    if second > first:
       return "Error: dont -"
    return first - second

def Multiplication(first, second):
    return first * second

def Division(first, second):
    if second == 0:
        return "Error: Division by zero is not allowed"
    return first / second

print(Addition(5, 2))
print(Subtraction(10, 50))
