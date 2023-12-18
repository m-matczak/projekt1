import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime
import random
import math


filepath = "random_numbers"


def ex_1():
    for i in range(1, 100):
        string = ""
        if i % 3 == 0:
            string += "Fizz"
        if i % 5 == 0:
            string += "Buzz"

        if string == "":
            print(i)
        else:
            print(string)


def ex_2():
    n = int(input("[Ex2] Input n how many numbers to generate: "))

    with open(filepath, "w") as file:
        for _ in range(0, n):
            r = random.randint(1, 10)
            file.write(f"{r}\n")


def ex_3():
    lines = []
    with open(filepath, "r") as file:
        for line in file.readlines():
            lines.append(int(line))

    sum = 0
    for line in lines:
        sum += line

    mean = sum / len(lines)

    variance = 0
    for line in lines:
        variance += (line - mean) ** 2

    stdev = math.sqrt(variance / len(lines))

    minimum = min(lines)
    maximum = max(lines)

    print("[Ex3]:")
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
    n = int(input("[Ex5] Input n: "))

    fib = []
    for i in range(1, n+1):
        fib.append(ex_4(i))

    plt.plot(fib)
    plt.title("Fibonacci numbers")
    plt.show()


def ex_6():
    n = int(input("[Ex6] Input n: "))

    d = {}
    for i in range(1, n+1):
        d[i] = i*i

    print(d)
    return d


def ex_7(d):

    s = 0
    for _, v in d.items():
        s += v
    print(s)


def ex_8():
    n = int(input("[Ex8] Input n:"))
    for _ in range(10):
        now = datetime.now()
        filename = now.strftime("%Y-%m-%d_%h-%M-%S-%f")
        with open(filename, "wb") as file:
            random_data = np.random.rand(n)
            file.write(bytearray(random_data))


def normalize(x):
    return np.sqrt(x.dot(x))


def ex_9():
    # wykresy
    data = np.genfromtxt('reference_trajectory.csv', delimiter=',')

    t = data[1:-1, 0]
    x = data[1:-1, 1]
    y = data[1:-1, 2]
    z = data[1:-1, 3]

    fig, axs = plt.subplots(3)
    fig.suptitle("Position in function of time")

    axs[0].plot(t, x)
    axs[1].plot(t, y)
    axs[2].plot(t, z)
    plt.show()

    # srednia
    print("[Ex9] Mean values of position:")
    print(np.mean(data[1:-1, 1:4], axis=0))

    # predkosc
    velocities = data[1:-1, 4:7]
    normalized = np.apply_along_axis(normalize, axis=1, arr=velocities)
    np.savetxt("velocity.csv", normalized)


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
