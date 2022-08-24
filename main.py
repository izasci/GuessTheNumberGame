import random
from art import logo
from replit import clear

def chosen_number():
  return random.randint(1,100) 

def calculate_attempts():
  """Function calculates how many attempts user has at the beginning after choosing difficulty level"""
  wrong_answer = True
  while wrong_answer == True:
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
      wrong_answer = False
      return 10
    elif level == "hard":
      wrong_answer = False
      return 5
    else:
      wrong_answer = True

def making_guess(attempts):
  print(f"You have {attempts} remaining to guess the number")
  guess = input("Make a guess: ")
  try: 
      int(guess)
      return int(guess)
  except ValueError:
      return False
  
  
def comparison(number):
  attempts = calculate_attempts()
  while attempts > 0:
    guess = making_guess(attempts)
    if guess == False:
      attempts = 0
      print("Don't play with me. You lose.")
    elif guess == number:
      attempts = 0
      print(f"You got it! The answer was {number}.")
    elif guess > number:
      attempts -= 1
      print("Too high.")
      if attempts > 0:
        print("Guess again.")
      else:
        print("You've run out of guesses. You lose.")
    elif guess < number:
      attempts -= 1
      print("Too low.")
      if attempts > 0:
          print("Guess again.")
      else:
        print("You've run out of guesses. You lose.")
  
  
def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  number = chosen_number()
  comparison(number)
  
again = True  
while again == True:
  game()
  end = input("Do you want to play again? y or n\n").lower()
  if end == "y":
    clear()
  else:
    again = False
    print("Ok, then...")