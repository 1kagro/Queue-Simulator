class MMS:
    def __init__(self, mu, lamb) -> None:
        self.mu = mu
        self.lamb = lamb
    
    def get_rho(self):
        return self.lamb / self.mu