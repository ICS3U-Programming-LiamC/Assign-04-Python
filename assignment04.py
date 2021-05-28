#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: May 26-27, 2021
# This program returns the lowest
# common multiple of 2 numbers


import math

def main():

    # vars
    user_num_str1 = input("number 1: ")
    user_num_str2 = input("number 2: ")
    # user_num_str3 = input("number 3: ")

    # make sure the users num can be an integer
    try:
        user_num1 = int(user_num_str1)
        user_num2 = int(user_num_str2)
        # user_num3 = int(user_num_str3)
    
        # FOR NUMBER 1 #############################
    
        # THIS CODE IS MOSTLY TAKEN FROM A WEBSITE THAT
        # DESCRIBES HOW TO FIND THE LCM OF ANY 2 NUMBERS
        
        new_user_num1 = user_num1
        list_of_nums = [1]
        
        # determines how many times the number can be divided by 2
        while (new_user_num1 % 2 == 0):
            new_user_num1 = (new_user_num1 / 2)
            list_of_nums.append(2)
            # print(list_of_nums)

        # now that the number is odd this code will determine more of the
        # prime factors past 2
        for i in range(3, int(math.sqrt(new_user_num1))+ 1, 2):
            
            # while i divides new_user_num , print i ad divide new_user_num
            while (new_user_num1 % i == 0):
                list_of_nums.append(i)
                # print(list_of_nums)
                new_user_num1 = new_user_num1 / i
        
        # this returns the last prime factor
        if new_user_num1 > 2:
            # print("{0:.0f}".format(new_user_num1))
            list_of_nums.append(new_user_num1)
            # print(list_of_nums)


        # FOR NUMBER 2 #############################

        # THIS CODE IS MOSTLY TAKEN FROM A WEBSITE THAT
        # DESCRIBES HOW TO FIND THE LCM OF ANY 2 NUMBERS
        
        new_user_num2 = user_num2
        list_of_nums2 = [1]
        
        # determines how many times the number can be divided by 2
        while (new_user_num2 % 2 == 0):
            new_user_num2 = (new_user_num2 / 2)
            list_of_nums2.append(2)
            # print(list_of_nums2)

        # now that the number is odd this code will determine more of the
        # prime factors past 2
        for i in range(3, int(math.sqrt(new_user_num2))+ 1, 2):
            
            # while i divides new_user_num , print i ad divide new_user_num
            while (new_user_num2 % i == 0):
                list_of_nums2.append(i)
                # print(list_of_nums2)
                new_user_num2 = new_user_num2 / i
        
        # this returns the last prime factor
        if new_user_num2 > 2:
            # print("{0:.0f}".format(new_user_num2))
            list_of_nums2.append(new_user_num2)
            # print(list_of_nums2)
            
        
        set1 = set(list_of_nums)
        set2 = set(list_of_nums2)
        final_set = {1}
        final_set2= {1}
        final_list = []
        
        for item in list_of_nums:
            final_list.append(item)
            
        for item in list_of_nums2:
            final_list.append(item)
        
        for item in set1:
            final_set.add(item)
        
        for item in set2:
            final_set.add(item)
            
        for item in final_list:
            final_set2.add(item)
        
        # print(set1)
        # print(set2)
            
        print(final_set)
        print(final_set2)
        print(final_list)
        # print(set1)
        
        lcm = 1
        
        for i in final_set2:
            lcm = lcm * i
            
        print(lcm)


    except ValueError:
        print("Not valid input")


if __name__ == "__main__":
    main()
