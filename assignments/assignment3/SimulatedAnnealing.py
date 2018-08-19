from math import log, exp, fabs, inf
from random import randint, random, seed
from os import system
import subprocess as sp
from time import sleep


class SimulatedAnnealing:
    """
    Queens are represented as a list of position
    E.g.: [1, 5, 3, 5, 2, 6, 0, 7] that is
    Queen in first column is in 2nd cell and
    Queen in 7th column is in 1st cell
    """

    def __init__(self, t_max=500., t_min=0, steps=500):
        self.T_max = t_max
        self.T_min = t_min
        # self.T_factor = -log(self.T_max / self.T_min)
        self.steps = steps
        self.T = t_max
        seed(1)

    def schedule(self, t):
        return self.T_max * exp(self.T_factor * t / self.steps)

    def schedule2(self, t):
        T = self.T_max - ((self.T_max - self.T_min) / self.steps) * t
        return T

    def anneal(self, initial_state=None, visualize=True, animation=False, log_output=None):
        if initial_state is None:
            current_state = self.random_initial_state()
        else:
            current_state = initial_state
        if log_output is None:
            log_output = animation

        t = 0
        while True:
            t += 1
            temperature = self.schedule2(t)
            # if temperature < self.T_min + 0.01:
            if temperature < 0:
                if visualize:
                    return self.tap(self.visualize, current_state)
                else:
                    return current_state
            next_state = self.random_successor(current_state)
            next_value = self.value(next_state)
            if next_value is inf:
                break
            current_value = self.value(current_state)
            d_energy = next_value - current_value

            if animation:
                # system("cls")
                sleep(1)
                tmp = sp.call('cls', shell=True)
            if log_output:
                self.visualize(current_state, {"ΔE": d_energy, "Time": t})

            if d_energy > 0:
                current_state = next_state
            elif exp(d_energy / temperature) > random():
                current_state = next_state

        if visualize:
            tmp = sp.call('cls', shell=True)
            return self.tap(self.visualize, current_state)
        else:
            return current_state

    @staticmethod
    def random_initial_state():
        state = [randint(0, 7) for i in range(8)]
        return state

    @staticmethod
    def random_successor(current):
        rand_queen = randint(0, 7)
        rand_move = randint(0, 7) - current[rand_queen]
        successor = [value for value in current]
        successor[rand_queen] += rand_move
        return successor

    @staticmethod
    def count_checks(state):
        checks = 0
        for i in range(8):
            for j in range(i + 1, 8):
                if state[i] is state[j]:
                    checks += 1
                elif fabs(SimulatedAnnealing.slop(i, state[i], j, state[j])) == 1:
                    checks += 1
        return checks

    @staticmethod
    def value(state):
        checks = SimulatedAnnealing.count_checks(state)
        if checks is 0:
            return inf
        return 56 / checks

    @staticmethod
    def slop(x1, y1, x2, y2):
        return (x1 - x2) / (y1 - y2)

    @staticmethod
    def tap(func, value):
        func(value)
        return value

    @staticmethod
    def visualize(state, params={}):
        printf = lambda *args: print(*args, end='')
        min_check = inf
        for i in range(8):
            printf("| ")
            for j in range(8):
                if state[j] is i:
                    printf("Q | ")
                else:
                    new_state = [value for value in state]
                    new_state[i] = j
                    check = SimulatedAnnealing.count_checks(new_state)
                    if check < min_check:
                        min_check = check
                    printf("{}{}| ".format(check, ' ' if check < 10 else ''))
            printf("\n")

        for key, check in params.items():
            print("{}: {}".format(key, check))
        printf("min check: {}".format(min_check))
        print("")


SimulatedAnnealing(steps=200).anneal(animation=True)
