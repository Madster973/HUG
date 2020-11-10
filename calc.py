# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 11:20:12 2020

@author: saima
"""

"""BASIC FUNCTIONS OF A CALCULATOR"""
def add(a:int,b:int) -> int:
    """addition of two numbers"""
    return a+b

def sub(a:int,b:int) -> int:
    """subract of two numbers"""
    return a-b

def product(a:int,b:int) -> int:
    """product of two numbers"""
    return a*b

def div(a:int,b:int) -> int:
    """division of two numbers"""
    return a/b

if __name__=='__main__':
    print(add(3,2.5))