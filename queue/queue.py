from .mm1 import MM1
from .mm1k import MM1K

class Queue:
    def __init__(self, lamb, mu, s = None, k = None) -> None:
        self.lamb = lamb
        self.mu = mu
        self.k = k
        self.s = s
        self.system_name = 'M/M/'
    
    def calculate_queue(self):
        if self.s is None:
            self.system_name += 'S'
        else:
            self.system_name += str(self.s)
        
        if self.k is not None:
            self.system_name += '/' + str(self.k)

        
        
        
