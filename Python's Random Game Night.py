import random

items = ["apple", "banana", "cherry", "date", "grape"]

selected_item = random.choice(items)

guess = input("Guess which item was selected from the list: ")

if guess.lower() == selected_item:
    print("Congratulations! You guessed correctly.")
else:
    print("Sorry, that's not correct. The selected item was:", selected_item)
