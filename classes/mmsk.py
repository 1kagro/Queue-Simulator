from math import factorial, sum, pow

class MMSK:
    
    def __init__(self, mu, lamb, s, k) -> None:
        self.mu = mu
        self.lamb = lamb
        self.s = s
        self.k = k
        self._rho = lamb / (self.s * mu)
        self.__rho = self.lamb / self.mu
        self.__lamb_eff = self.lamb * (k - self.get_l())
    
    def get_rho(self):
        return self.lamb / (self.mu * self.k)
    
    def get_pn(self, n: int):
        """
        Returns the probability of having n customers in the system.
        """
        if n > self.k:
            return 0
        
        if n == 0:
            return 1 / ((sum(pow(self.__rho, _n)/factorial(_n)) for _n in range(0, self.s)) + (pow(self.__rho, self.s)/factorial(self.s)) * (sum(pow(self.__rho / (self.s * self.mu), _n - self.s) for _n in range(self.s + 1, self.k))))

        if n < self.s:
            return (pow(self.__rho, n)/factorial(n)) * self.get_pn(0)

        return (pow(self.__rho, n)/(factorial(self.s)*pow(self.s, n - self.s))) * self.get_pn(0)

    def get_lq(self):
        """
        Returns the expected number of customers in the queue.
        """
        return int(sum((n - self.s) * self.get_pn(n)) for n in range(self.s + 1, self.k))

    def get_l(self):
        """
        Returns the expected number of customers in the system.
        """
        return self.get_lq() + (self.__lamb_eff / self.mu)
    
    def get_wq(self):
        """
        Returns the expected time a customer spends in the queue.
        """
        return self.get_lq() / self.__lamb_eff
    
    def get_w(self):
        """
        Returns the expected time a customer spends in the system.
        """
        return self.get_wq() + (1 / self.mu)