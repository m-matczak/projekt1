import matplotlib.pyplot as plt
import numpy as np
import random
import statistics
from datetime import datetime
import csv

filepath = "random_numbers"

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
    n = int(input("Input how many numbers to generate: "))

    with open(filepath, "w") as file:
        for _ in range(0,n):
            r = random.randint(1,10)
            file.write(f"{r}\n")

def ex_3():
    lines = []
    with open(filepath, "r") as file:
        for line in file.readlines():
            lines.append(int(line))


    mean = statistics.fmean(lines)
    stdev = -1
    if len(lines) != 1:
        stdev = statistics.stdev(lines)
    minimum= min(lines)
    maximum = max(lines)

    print(f"mean: {mean}")
    print(f"stdev: {stdev}")
    print(f"minimum: {minimum}")
    print(f"maximum: {maximum}")

def ex_4(n):
    if n in {0, 1}:
        return n
    n = ex_4(n-1) + ex_4(n-2)
    return n

def ex_5():
    n = int(input("Podaj liczbe n: "))

    fib = []
    for i in range(1,n):
        fib.append(ex_4(i))

    plt.plot(fib)
    plt.ylabel("Fibonacci numbers")
    plt.show()

def ex_6():
    n = int(input("Podaj liczbe n: "))

    d = {}
    for i in range(1,n+1):
        d[i] = i*i

    print(d)
    return d

def ex_7(d):

    s = 0
    for _, v in d.items():
        s += v
    print(s)

def ex_8():
    n = int(input("Podaj n liczb losowych:"))
    for fn in range(10):
        now = datetime.now()
        filename = now.strftime("%Y-%m-%d_%h-%M-%S-%f")
        with open(filename, "wb") as file:
            random_data = np.random.rand(n)
            file.write(bytearray(random_data))

def ex_9():
    pass

def main():
    ex_1()
    ex_2()
    ex_3()
    ex_5()
    d = ex_6()
    ex_7(d)
    ex_8()
    ex_9()

if __name__ == '__main__':
    main()
