import numpy as np

def calculate(array):
    fitness = schwefel(array)
    return fitness

def schwefel(array):
    sum = 0
    fitness = 0
    for x in array:
        sum = sum + x * np.sin(np.sqrt(np.abs(x)))
    fitness = 418.9829 * len(array) - sum
    return fitness
if __name__ == "__main__":
    print("You are in the cost function file.")
