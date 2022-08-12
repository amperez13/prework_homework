#Question 1: Write a function to print 
#"hello_USERNAME!" USERNAME is the input of the function
def hello_name(user_name):
    for name in user_name:
        msg = "hello_" +name.upper() + "!"
        print(msg)
user_name = ['username']
hello_name(user_name)

#Question 2: prints odd numbers from 1-100, returning nothing
def first_odds():
    