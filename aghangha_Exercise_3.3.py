#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on January 15 2020
by Ankit Ghanghas

Exercise 3.3 Think Python Chapter 3

This program prints out a  2X2 and a 4X4 grid made up of +, - and | elemts for joint, row and 
column respectively.

"""
# this function takes an argument "f" (a function object) as input and repeats the function
# object twice
def do_twice(f):
    f()
    f()
# this function takes an argument "f" (a funciton object) as input and repeats the function four times
def four(f):
    do_twice(f)
    do_twice(f)
# this funciton prints the basic building block of the beam "-" and allows the next output to be 
# printed in the same line.    
def h_unit():
    print('-',end='')
# this funciton prints the basic unit for a row "+----" and allows the next output to be printed
# in the same line
def row_unit():
    print('+' ,end='')
    do_twice(h_unit)
    do_twice(h_unit)
# this funciton prints an entire row "+----+----+" for a two grid floor 
def row():
    do_twice(row_unit)
    print('+')
# this funciton makes partial column with just one unit "|    " (part of the row)
def pcol_unit():
    print('|    ',end='')
# this function makes pratial column units for the entire row for a two grid "|    |    |"
def col_unit():
    do_twice(pcol_unit)
    print('|')
# make an entire column made up of four column units
def col():
    four(col_unit)
# makes an entire floor with a complete two grid row on top and a two grid column (with four column_units)
# below it
def floor():
    row()
    col()
# function that gives out an entire 2X2 grid made of the desired elements.
def two_grid():
    do_twice(floor)
    row()

two_grid()

#part 2 four_grid

# this funciton prints an entire row "+----+----+" for a four grid floor 
def row1():
    four(row_unit)
    print('+')
    
# this function makes pratial column units for the entire row for a four grid "|    |    |    |    |"
def col_unit1():
    four(pcol_unit)
    print('|')
# make an entire column  made up of four column units (the ones for a four grid)
def col1():
    four(col_unit1)

# makes an entire floor with a complete four grid row on top and a two grid column (with four column_units)
# below it
def floor1():
    row1()
    col1()
    
# function that gives out an entire 4X4 grid made of the desired elements.
def four_grid():
    four(floor1)
    row1()
four_grid()
