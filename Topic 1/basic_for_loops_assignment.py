"""
Program: basic_for_loops_assignment.py
Author: Alex Heinrichs
Last date modified: 09/25/2022

Simple code to declare a list of floating point numbers,
write a for loop to print each, and the writing a second
for loop to print each odd number descending from 99 to 33
(including 99 and 33)
"""

# Declare a list of floating point numbers
float_list = [1.3, 5.2, 7.3, 5.8, 21.6, 764.56, 43.75]

# Write a for loop to print each
for float_num in float_list:
    print(float_num)

# Write a second for loop to print the odd number
# descending from 99 to 33 (including 99 and 33)
for odd in range(99, 32, -1):  # goes to 32 to include 33
    # if statement asks is variable odd (% 2 != 0)
    if odd % 2 != 0:
        print(odd)
