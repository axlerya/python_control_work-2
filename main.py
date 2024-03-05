from toysmanager import *


class Main:

    sys = ToySystem()
    manager = ToysManager()

    def add_toy(self,name: str, count: int, priority: int):
        self.sys.add_toys_in_system(name, count, priority)

    def change_priority(self, id: int, priority: int):
        self.sys.change_priority(id, priority)
    
    def lottery(self):
        self.manager.lottery()
        
    def give_toys(self):
        self.manager.give_toys()
    
    
main = Main()

while True:
    print('''
        =============================
        1 - добавить игрушку в автомат"
        2 - изменить приоритет выпаденеия по id
        3 - розыгрыш
        4 - получить игрушки
        5 - выход
        =============================
          ''')
    command = input("Введите команду")

    match command:
        
        case '1':
            name = input('введите имя игрушки')
            count = int(input('введите количество'))
            priority = int(input('введите приоретет'))
            main.add_toy(name, count, priority)

        case '2':
            id = int(input('введите id'))
            priority = int(input('введите приоретет'))
            main.change_priority(id, priority)

        case '3':
            main.lottery()

        case '4':
            main.give_toys()

        case '5':
            break

        case _:
            print("Некорректный ввод команды")
