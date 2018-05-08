import numpy as np
import math
from Params import params as ps
import fitness as ft

def levy_flight(Lambda):
        sigma1 = np.power((math.gamma(1 + Lambda) * np.sin((np.pi * Lambda) / 2)) / math.gamma((1 + Lambda) / 2) * np.power(2, (Lambda - 1) / 2), 1 / Lambda)
        sigma2 = 1
        u = np.random.normal(0, sigma1, size = ps.get_dims())
        v = np.random.normal(0,sigma2, size = ps.get_dims())
        
        step = u / np.power(np.fabs(v),1/Lambda)
        
        return step
class Cuckoo_eval:
    def __init__(self):
        self.position = np.random.rand(ps.get_dims()) * (ps.get_maxD() - ps.get_minD()) + ps.get_minD()
        self.fitness = ft.calculate(self.position)
    
    def get_position(self):
        return self.position
    
    def set_position(self, newPosition):
        self.position = newPosition
    
    def get_fitness(self):
        return self.fitness
    
    def set_fitness(self, newFitness):
        self.fitness = newFitness
    
    def abandon(self):
        for i in range(len(self.position)):
            p = np.random.rand()
            if p < ps.get_pd():
                self.position[i] = np.random.rand() * (ps.get_maxD() - ps.get_minD()) + ps.get_minD()
    
    def get_cuckoo(self):
        step_size = ps.get_stepsize() * levy_flight(ps.get_Lambda())
        self.position = self. position + step_size
        
        for i in range(len(self.position)):
            if self.position[i] > ps.get_maxD(): self.position[i] = ps.get_maxD()
            if self.position[i] < ps.get_minD(): self.position[i] = ps.get_minD()
    
                