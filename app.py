from abc import ABC, abstractmethod
import itertools
import random
from time import sleep

class CassaNiquel:

    def __init__(self, level=1, balance=0):
        self.SIMBOLOS = {
            'money_mouth_face': '1F911',
            'cold_face': '1F976',
            'alien': '1F47D',
            'heart_on_fire': '2764',
            'collision': '1F4A5'
        }
        self.level = level
        self.permutations = self._gen_permutations()
        self.balance = 0
        self.initial_balance = self.balance


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
        
        return result

    def _display(self, amount_bet, result, time=0.1):
        seconds = 1
        for i in range(0, int(seconds/time)):
            print(self._emojize(random.choice(self.permutations)))
            sleep(time)
        print(self._emojize(result))

        if self._check_result_user(result):
            print(f'Você venceu e recebeu: {amount_bet*3}')
        else:
            print('foi quase, tente novamente.')

    def _emojize(self, emojis):
        return ''.join(tuple(chr(int(self.SIMBOLOS[code], 16)) for code in emojis))

    def _check_result_user(self, result):
        x = [result[0] == x for x in result]
        return True if all(x) else False      

    def _update_balance(self, amount)



maquina1 = CassaNiquel()
maquina1._display(0, maquina1._get_final_result())