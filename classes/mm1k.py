from utils.Decorator import round_to_decimals

class MM1K:
    
    def __init__(self, mu: float, lamb: float, k: int) -> None:
        self.mu = mu
        self.lamb = lamb
        self.k = k
        self._rho = self.lamb / self.mu
        self.lamb_eff = self.lamb * (1 - self.get_pn(self.k))
    
    @round_to_decimals(3)
    def get_rho(self):
        return self._rho
    
    @round_to_decimals(3)
    def get_pn(self, n: int):
        """
        Returns the probability of having n customers in the system.
        """
        
        if n < 0:
            return "n must be greater than or equal to 0"
        
        if self._rho == 1:
            return 1 / (self.k + 1)
        
        return ((1 - self._rho) / (1 - self._rho ** (self.k + 1))) * (self._rho ** n)
    
    @round_to_decimals(3)
    def get_l(self):
        """
        Returns the expected number of customers in the system.
        """
        if self._rho == 1:
            return self.k / 2
        return (self._rho / (1 - self._rho)) - (((self.k + 1) * (self._rho ** (self.k + 1))) / (1 - self._rho ** (self.k + 1)))
    
    @round_to_decimals(3)
    def get_lq(self):
        """
        Returns the expected number of customers in the queue.
        """
        return self.get_l() - (1 - self.get_pn(0))
    
    @round_to_decimals(3)
    def get_w(self):
        """
        Returns the expected time a customer spends in the system.
        """
        return self.get_l() / self.lamb_eff
    
    @round_to_decimals(3)
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