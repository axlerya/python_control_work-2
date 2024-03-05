from toys import Toys
from toysytem import ToySystem
from random import choice


class ToysManager(ToySystem):

    _list_toys = []

    def lottery(self):
        priority_list = []
        toys_in_sytem = self.get_toys_list_in_system()

        for toy in toys_in_sytem:
            priority_list.append(toy._priority)

        toys_index = [index for index, value in enumerate(priority_list)
            if value == min(priority_list)]
        
        try:
            win_index = choice(toys_index)
        except: 
            return print('Игрушки закончились')
        
        toy_win = self._toys_list_in_system[win_index]
        
        self._list_toys.append(toy_win)
        toy_win.reduce_count(1)
        
        self.check_count()
        print(f'Вы получили {toy_win}')

    def give_toys(self):
        
        with open('toys.txt', 'a', encoding='utf-8') as f:
            for i in  range(len(self._list_toys)):
                toy = self._list_toys[i]
                data = f"""
=======================
Игрушка: 
    название: {toy._name}
    id: {toy._id}
    приоритет: {toy._priority}
+++++++++++++++++++++++
"""
                f.write(data)
            f.close()
        self._list_toys.clear()
