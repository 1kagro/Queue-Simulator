from .mm1 import MM1
from .mms import MMS
from .mm1k import MM1K
from .mmsk import MMSK

from utils.Exception import InvalidAPIUsage

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
            model_attrs = {'mu': self.mu, 'lamb': self.lamb}
            
            if self.k not in [None, 0]:
                self.system_name += f'/{self.k}'
                model_class = MM1K if self.s == 1 else MMSK
                model_attrs['k'] = self.k
                if model_class == MMSK:
                    model_attrs['s'] = self.s
            else:
                model_class = MM1 if self.s == 1 else MMS
                if model_class == MMS:
                    model_attrs['s'] = self.s
                
            model = model_class(**model_attrs)
            print(self.system_name, model.get_rho())
            if 0 > model.get_rho() > 1 :
                raise InvalidAPIUsage('The system is unstable')
            print(model.__class__)
            response = {
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
                'pn': []
            }
            
            if self.k not in [None, 0]:
                response['pn'] = [model.get_pn(n) for n in range(0, self.k + 1)]
            else:
                last_probability = 0
                n = 0
                while last_probability <= 1:
                    last_probability = model.get_pn(n)
                    response['pn'].append(model.get_pn(n))
                    n += 1
                    print('n', n)
                    print(last_probability)
                # pass
            
            print(response)
            return response
        except Exception as e:
            raise e
