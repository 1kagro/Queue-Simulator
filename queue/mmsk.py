import math

class MMMSK:
    
    def __init__(self, mu, lamb, k) -> None:
        self.mu = mu
        self.lamb = lamb
        self.k = k
    
    def get_rho(self):
        return self.lamb / (self.mu * self.k)
    
    def get_p0(self):
        rho = self.get_rho()
        return 1 / (sum([(rho ** i) / math.factorial(i) for i in range(self.k + 1)]) + (rho ** (self.k + 1)) / (math.factorial(self.k) * (self.k - rho)))
    