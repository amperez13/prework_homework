#Question 1: Write a function to print 
#"hello_USERNAME!" USERNAME is the input of the function

def hello_name(user_name):
    for name in user_name:
        msg = "hello_" +name.upper() + "!"
        print(msg)
user_name = ['username']
hello_name(user_name)

#adapted from greet_users exercise in chapter 8


#Question 2: prints odd numbers from 1-100, returning nothing

def first_odds(n): 
    return [x for x in range(1, n+1) if x % 2 == 1]

print(first_odds(100))

#In the try it for chapter 4, we did it differently, and would sub out the 21 for 100
#odd_numbers = list(range(1,21,2))
#print(odd_numbers)
#I looked at code from the following URL and adapted to use the def function:
#https://stackoverflow.com/questions/66415022/print-the-odd-number-using-list-comprehension


#Question 3 write a python function max_num _in_list to return the max number of a list

def max_num_in_list(a_list):
    max = a_list[0]
    for x in a_list:
        if x > max:
            max = x
    return max

a_list = [13, 17, 77, 1138]
print("\nThe largest number in the list is ", max_num_in_list(a_list))

#I looked at the different ways to use the max() function but ended up using 
#and adapting code I found here: https://www.geeksforgeeks.org/python-program-to-find-largest-number-in-a-list/


#Question 4 Write a function to return if the given year is a leap year, given
# the following parameters: divisible by 4, but not 100 unless also divisible by 400
#Boolean Return

def is_leap_year(a_year):
    if a_year % 400 == 0:
        return True
    if a_year % 100 == 0:
        return False
    if a_year % 4 == 0:
        return True
    return False
print(is_leap_year(1900))

# Adapted from code found here: 
#https://stackoverflow.com/questions/11621740/how-to-determine-whether-a-year-is-a-leap-year
#also, I discovered that there is a calendar function for this (calendar.isleap)
#I would have preferred to answer the questiuon like this:
#def is_leap_year(a_year):
    #return (a_year % 4 == 0 and a_year % 100 != 0) or a_year % 400 == 0
#a_year = 1900
#print a_year, " is a leap year" if is_leap_year(a_year) else " is not a leap year"


#Question 5 write a finction to check if all numbers in a list are consecutive. 
#Boolean Return
#changed the list name because used previously

def is_consecutive (b_list):
    return sorted(b_list) == list(range(min(b_list), max(b_list)+1))

b_list = [1, 2, 4, 5]
print(is_consecutive(b_list))

#code adapted from https://www.geeksforgeeks.org/python-check-if-list-contains-consecutive-numbers/
