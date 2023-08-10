from utils.Decorator import round_to_decimals
class MM1:
    def __init__(self, mu: float, lamb: float) -> None:
        self.mu = mu
        self.lamb = lamb
        self._rho = lamb / mu
    
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
            return 1 / (n + 1)
        
        return ((1 - self._rho) * (self._rho ** n))
    
    @round_to_decimals(3)
    def get_l(self):
        """
        Returns the expected number of customers in the system.
        """
        if self._rho == 1:
            return 1 / (1 - self._rho)
        
        return self.lamb / (self.mu - self.lamb)
    
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
        return self.get_l() / self.lamb
    
    @round_to_decimals(3)
    def get_wq(self):
        """
        Returns the expected time a customer spends in the queue.
        """
        return self.get_lq() / self.lamb