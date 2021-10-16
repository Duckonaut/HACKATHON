import math
from typing import Callable, List
import random

import numpy

DATASET = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
LEARN_COUNT = 1000

# two input nodes, one output
# output node has 3 weights, input0, input1 and bias

def simpleActivation(x: float) -> float:
    if x > 0:
        return 1
    
    return 0

def sigmoidActivation(x: float) -> float: # funny truthy/falsy version
    return 1 / (1 + numpy.exp(-x))

class BooleanNetwork:
    def __init__(self, activationFunction: Callable[[float], float]):
        self.bias = random.random()
        self.weights = [random.random(), random.random(), random.random()]
        self.activationFunction = activationFunction
    
    def learn(self, input0: int, input1: int, output: int) -> None:
        unscaledOutput = input0 * self.weights[0] + input1 * self.weights[1] + self.bias * self.weights[2]

        currentOutput = self.activationFunction(unscaledOutput)

        error = output - currentOutput

        self.weights[0] += error * input0
        self.weights[1] += error * input1
        self.weights[2] += error * self.bias

    def calculate(self, input0: int, input1: int) -> float:
        unscaledOutput = input0 * self.weights[0] + input1 * self.weights[1] + self.bias * self.weights[2]

        return self.activationFunction(unscaledOutput)

def calculateAccuracy(network: BooleanNetwork, dataset: List[List[int]]) -> float:
    testNumber = len(dataset)

    cumulativeError = 0

    for r in dataset:
        cumulativeError = cumulativeError + abs(r[2] - network.calculate(r[0], r[1]))
            
    
    return 1 - cumulativeError / testNumber

    

def main():
    simpleNetwork = BooleanNetwork(simpleActivation)
    sigmoidNetwork = BooleanNetwork(sigmoidActivation)

    print(f'Simple starting weights: {simpleNetwork.weights}')
    print(f'Sigmoid starting weights: {sigmoidNetwork.weights}')
    print(f'Simple bias: {simpleNetwork.bias}')
    print(f'Sigmoid bias: {sigmoidNetwork.bias}')

    for _ in range(LEARN_COUNT):
        for r in DATASET:
            simpleNetwork.learn(*r)
            sigmoidNetwork.learn(*r)

    print(f'Finished simple weights: {simpleNetwork.weights}')
    print(f'Finished sigmoid weights: {sigmoidNetwork.weights}')

    print(f'Simple accuracy: {calculateAccuracy(simpleNetwork, DATASET)}')
    print(f'Sigmoid accuracy: {calculateAccuracy(sigmoidNetwork, DATASET)}')

if __name__ == '__main__':
    main()