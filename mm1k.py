import math

class MMM1K:
    
    def __init__(self, mu, lamb, k) -> None:
        self.mu = mu
        self.lamb = lamb
        self.k = k
        self._rho = self.lamb / self.mu
        self.lamb_eff = self.lamb * (1 - self.get_pn(self.k))
    
    def get_rho(self):
        return self._rho
    
    def get_pn(self, n: int):
        """
        Returns the probability of having n customers in the system.
        """
        
        if n < 0:
            return "n must be greater than or equal to 0"
        
        if self._rho == 1:
            return 1 / (self.k + 1)
        
        return ((1 - self._rho) / (1 - self._rho ** (self.k + 1))) * (self._rho ** n)
    
    
    def get_l(self):
        """
        Returns the expected number of customers in the system.
        """
        if self._rho == 1:
            return self.k / 2
        
        return (self._rho / 1 - self._rho) - (((self.k + 1) * (self._rho ** (self.k + 1))) / (1 - self._rho ** (self.k + 1)))
    
    def get_lq(self):
        """
        Returns the expected number of customers in the queue.
        """
        return self.get_l() - (1 - self.get_pn(0))
    
    def get_w(self):
        """
        Returns the expected time a customer spends in the system.
        """
        return self.get_l() / self.lamb_eff
    
    def get_wq(self):
        """
        Returns the expected time a customer spends in the queue.
        """
        return self.get_lq() / self.lamb_eff
    
    def result(self):
        return print(f"""
                System: M/M/1/{self.k}
                Customer arrival rate Lambda: {self.lamb}
                Customer service rate Mu: {self.mu}
                Number of servers: {self.k}
                Utilization factor: {self.get_rho()}
                Expected number of customers in the system: {self.get_l()}
                Expected number of customers in the queue: {self.get_lq()}
                Expected time a customer spends in the system: {self.get_w()}
                Expected time a customer spends in the queue: {self.get_wq()}
            """)

s = MMM1K(lamb=18, mu=6, k=4)
s.result()