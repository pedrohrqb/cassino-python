from abc import ABC, abstractmethod
import itertools
import random


def BaseMachine(ABC):
    @abstractmethod
    def _gen_permutations(self):
        pass

    @abstractmethod
    def _get_final_result(self):
        pass
    
    @abstractmethod
    def _display(self):
        pass

    @abstractmethod
    def _check_result_user(self):
        pass

    @abstractmethod
    def _update_balance(self):
        pass    

    @abstractmethod
    def emojize(self):
        pass

    @abstractmethod
    def gain(self):
        pass

    @abstractmethod
    def play(self, amount_bet, player):
        pass


class CassaNiquel:

    def __init__(self, level=1):
        self.SIMBOLOS = {
            'money_mouth_face': '1F911',
            'cold_face': '1F976',
            'alien': '1F47D',
            'heart_on_fire': '2764',
            'collision': '1F4A5'
        }
        self.level = level
        self.permutations = self._gen_permutations()
    
    def _gen_permutations(self):
        permutations = list(itertools.product(self.SIMBOLOS.keys(), repeat=3))
        for j in range(self.level):
            for i in self.SIMBOLOS.keys():
                permutations.append((i, i, i))        
        return permutations

    def _get_final_result(self):
        if not hasattr(self, 'permutations'):
            self.permutations = self._gen_permutations()

        result = list(random.choice(self.permutations))
        
        if len(set(result)) == 3 and random.randint(0, 5) >= 2:
            result[1] = result[0]

        

maquina1 = CassaNiquel()
maquina1._get_final_result()