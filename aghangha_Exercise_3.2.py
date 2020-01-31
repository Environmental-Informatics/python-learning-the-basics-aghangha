
"""
Created on January 15 2020
by Ankit Ghanghas

Exercise 3.2 Think Python Chapter 3

This program establishes two functions. The first one "do_twice" function which takes two arguments, 
one funciton object and a value and repeats the function object with value as its argument.The
second function "print_twice" takes one argument and prints it twice.
"""
# this function takes two arguments: function object "f" and value "g" and repeats the function object
# "f" twice with g as argument
def do_twice(f,g):
    f(g)
    f(g)
# this function prints the word "spam" once when called upon
def print_spam():
    print('spam')
#this function takes an argument value "a" and prints it twice 

def print_twice(a):
    print(a)
    print(a)
# here we apply the do_twice function with print_twice as the input funciton object and 'spam' as the argument
do_twice(print_twice,'spam')