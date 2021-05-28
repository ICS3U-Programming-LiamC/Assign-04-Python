#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: May 26-27, 2021
# This program returns the lowest
# common multiple of 2 numbers


# import the math module
import math


# define all the lists
list_of_nums = []
end_list = []
final_list = []


# main function
def main():
    number_of_processes = 0

    # vars
    user_num_str1 = input("number 1: ")
    user_num_str2 = input("number 2: ")
    counter = 1

    # make sure the users num is a num
    try:
        user_num1 = int(user_num_str1)
        user_num2 = int(user_num_str2)

        # determine the largest number the lcm should be
        max_num = user_num1*user_num2

        # make a new variable just so I dont change the original
        # I dont believe this was actually necessary
        divided_num = max_num

        # determin which of the two is larger than the other
        if (user_num1 > user_num2):
            bigger_num = user_num1
            smaller_num = user_num2
        else:
            bigger_num = user_num2
            smaller_num = user_num1

        # THIS IS WHERE IT GETS CONFUSING

        # this code figures out all the possible combinations of
        # the two inputs by dividing them by all the smaller of the two inputs
        for each in range(1, smaller_num + 1):
            divided_num = max_num / each
            list_of_nums.append(divided_num)
            number_of_processes = number_of_processes + 1

        # this is the final code
        # it filters out all numbers that cant be divided by the larger user
        # input and the smaller user input.
        for each in list_of_nums:
            number_of_processes = number_of_processes + 1
            if (each % bigger_num == 0) and (each % smaller_num == 0):
                final_list.append(each)

        # this code then takes the smallest number that passed
        # all those steps and then prints it to the suer
        lmc = min(final_list)
        print("The lowest common multiple of {0} and {1} is {2:.0f}".
              format(user_num1, user_num2, lmc))
        print("{} many processes were excecuted during this code".
              format(number_of_processes))

    # if the users input is not valid
    except ValueError:
        print("Not valid input")


if __name__ == "__main__":
    main()
