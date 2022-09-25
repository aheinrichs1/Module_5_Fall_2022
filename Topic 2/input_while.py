"""
Program: input_while.py
Author: Alex Heinrichs
Last date modified: 09/25/2022

Writing code to input a user entry into a list, and reasking
"""

user_list = []
user_input = input('Please enter a number from 0-100,'
                       ' enter -1 to quit: ')
while int(user_input) != -1:
    while int(user_input) < -1 or int(user_input) > 100:
        user_input = input("Invalid input, please enter a value from 0-100, "
                           "enter -1 to quit: ")
    user_list.append(int(user_input))
    print("Input " + str(user_input) + " added to list.")
    user_input = int(input('Please enter a number from 0-100,'
                       ' enter -1 to quit: '))
print(user_list)
