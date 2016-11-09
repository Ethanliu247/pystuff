#!/usr/bin/python3
from random import randint
from threading import Thread

def length(l):
    return range(len(l))

def randfloat(r1, r2, precision=1):
    p = precision
    r1*=10**p
    r2*=10**p
    rand = randint(r1, r2)
    return rand/10**(p)

class Node:
    def __init__(self, n=2):
        self.weights = list([0 for i in range(n)])
        self.c = 0.0000025
        for i in length(self.weights):
            self.weights[i] = randfloat(-1, 1)
    def feed(self, inputs):
        s = 0
        inputs = list(inputs)
        for i in length(self.weights):
            s += inputs[i]*self.weights[i]
        return self.activate(s)
    def activate(self, s):
        if s > 0: return 1
        else: return -1
    def train(self, inputs, answer):
        guess = self.feed(inputs)
        error = answer - guess
        for i in length(self.weights):
            self.weights[i] += self.c*error*inputs[i]
    def trainer(self, trainer):
        guess = self.feed(trainer.inputs)
        error = trainer.answer - guess
        for i in length(self.weights):
            self.weights[i] += self.c*error*trainer.inputs[i]

class Trainer:
    def __init__(self, x, y, answer):
        self.inputs = [x, y]
        self.answer = answer

n1 = Node()
