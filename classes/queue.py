from .mm1 import MM1
from .mms import MMS
from .mm1k import MM1K
from .mmsk import MMSK
class Queue:
    def __init__(self, lamb, mu, s = None, k = None) -> None:
        self.lamb = lamb
        self.mu = mu
        self.k = k
        self.s = s
        self.system_name = 'M/M/'
    
    def calculate_queue(self) -> dict:
        try:
            self.system_name += str(self.s)
            
            if self.k not in [None, 0]:
                self.system_name += f'/{self.k}'
                model_class = MM1K if self.s == 1 else MMSK
            else:
                model_class = MM1 if self.s == 1 else MMS
            
            model = model_class(self.mu, self.lamb, self.k) if self.k not in [None, 0] else model_class(self.mu, self.lamb)
            
            if model.get_rho() >= 1:
                raise Exception('The system is unstable')
            
            return {
                'system_name': self.system_name,
                'lamb': self.lamb,
                'mu': self.mu,
                'k': self.k,
                's': self.s,
                'rho': model.get_rho(),
                'l': model.get_l(),
                'lq': model.get_lq(),
                'w': model.get_w(),
                'wq': model.get_wq(),
                'p0': model.get_pn(0),
                'pn': [model.get_pn(i) for i in range(1, self.k + 1)],
            }
        except Exception as e:
            raise e
