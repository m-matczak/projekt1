import matplotlib.pyplot as plt
import numpy as np


def ex_1():
    for i in range(1,100):
        string = ""
        if i % 3 == 0:
            string = string + "Fizz"
        if i % 5 == 0:
            string = string + "Buzz"

        if string == "":
            print(i)
            continue
        else:
            print(string)

def ex_2():
    pass

def ex_3():
    pass

def ex_4(n):
    return n

def ex_5():
    pass

def ex_6():
    pass

def ex_7():
    pass

def ex_8():
    pass

def ex_9():
    pass


def main():
    ex_1()
    ex_2()
    ex_3()
    ex_5()
    ex_6()
    ex_7()
    ex_8()
    ex_9()

if __name__ == '__main__':
    main()
