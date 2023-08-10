from math import factorial, pow
from utils.Decorator import round_to_decimals

class MMS:
    def __init__(self, mu, lamb, s) -> None:
        self.mu = mu
        self.lamb = lamb
        self.s = s
        self._rho = lamb / (self.s * mu)
        self.__rho = self.lamb / self.mu

    @round_to_decimals()
    def get_rho(self):
        return self._rho

    @round_to_decimals()
    def get_pn(self, n: int):
        """
        Returns the probability of having n customers in the system.
        """
        if n == 0:
            return 1 / (sum([pow(self.__rho, _n)/factorial(_n) for _n in range(0, self.s)]) + (pow(self.__rho, self.s)/factorial(self.s))*((self.s*self.mu)/(self.s*self.mu - self.lamb)))

        if n <= self.s:
            return (pow(self.__rho, n)/factorial(n)) * self.get_pn(0)

        return (pow(self.__rho, n)/(factorial(self.s)*pow(self.s, n - self.s))) * self.get_pn(0)

    @round_to_decimals()
    def get_lq(self):
        """
        Returns the expected number of customers in the queue.
        """
        return (pow(self.__rho, self.s) / factorial(self.s)) * (self._rho / (pow(1 - self._rho, 2))) * self.get_pn(0)

    @round_to_decimals()
    def get_l(self):
        """
        Returns the expected number of customers in the system.
        """
        return self.get_lq() + self.__rho

    @round_to_decimals()
    def get_wq(self):
        """
        Returns the expected time a customer spends in the queue.
        """
        return self.get_lq() / self.lamb

    @round_to_decimals()
    def get_w(self):
        """
        Returns the expected time a customer spends in the system.
        """
        return self.get_wq() + (1 / self.mu)
