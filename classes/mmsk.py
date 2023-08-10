from math import factorial, pow
from utils.Decorator import round_to_decimals

class MMSK:
    
    def __init__(self, mu, lamb, s, k) -> None:
        self.mu = mu
        self.lamb = lamb
        self.s = s
        self.k = k
        self._rho = lamb / (self.s * mu)
        self.__rho = self.lamb / self.mu
        self.__lamb_eff = self.lamb * (k - self.get_l())
    
    @round_to_decimals(3)
    def get_rho(self):
        return self.lamb / (self.mu * self.k)
    
    @round_to_decimals(3)
    def get_pn(self, n: int):
        """
        Returns the probability of having n customers in the system.
        """
        if n > self.k:
            return 0
        
        if n == 0:
            return 1 / (sum([pow(self.__rho, _n)/factorial(_n) for _n in range(0, self.s + 1)]) + (pow(self.__rho, self.s)/factorial(self.s)) * sum([pow(self.__rho / (self.s * self.mu), _n - self.s) for _n in range(self.s + 1, self.k + 1)]))

        if n < self.s:
            return (pow(self.__rho, n)/factorial(n)) * self.get_pn(0)

        return (pow(self.__rho, n)/(factorial(self.s)*pow(self.s, n - self.s))) * self.get_pn(0)

    @round_to_decimals(3)
    def get_lq(self):
        """
        Returns the expected number of customers in the queue.
        """
        return sum([(n - self.s) * self.get_pn(n) for n in range(self.s + 1, self.k + 1)])
    
    @round_to_decimals(3)
    def get_l(self):
        """
        Returns the expected number of customers in the system.
        """
        return self.get_lq() + (self.__lamb_eff / self.mu)
    
    @round_to_decimals(3)
    def get_wq(self):
        """
        Returns the expected time a customer spends in the queue.
        """
        return self.get_lq() / self.__lamb_eff
    
    @round_to_decimals(3)
    def get_w(self):
        """
        Returns the expected time a customer spends in the system.
        """
        return self.get_wq() + (1 / self.mu)