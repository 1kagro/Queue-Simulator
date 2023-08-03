class MM1:
    def __init__(self, _lambda, mu) -> None:
        self._lambda = _lambda
        self.mu = mu
        self.rho = _lambda / mu
        self.p0 = 1 - self.rho
        self.Lq = self.rho ** 2 / (1 - self.rho)