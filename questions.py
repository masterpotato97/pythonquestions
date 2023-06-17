#Write a function to print “hello_USERNAME!” USERNAME is the input of the function. The first line of the code has been defined as below.


def hello(name):
    return 'Hello '+ name

#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for x in range(1, 101):
        if x % 2 == 0:
            continue
        else:
            print(x)