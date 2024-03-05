from toys import Toys


class ToySystem:

    _toys_list_in_system = []

    def add_toys_in_system(self, name: str, count: int, priority: int):
        self._toys_list_in_system.append(
            Toys(self.get_free_id(), name, count, priority))

    def change_priority(self, id: int, priority: int):
        for i in self._toys_list_in_system:
            if i._id == id:
                i.edit_priority(priority)
                print(f'Выизменили приорет игрушки: {i._name}')

    def check_count(self):
        for i in self._toys_list_in_system:
            if i._count <= 0:
                self._toys_list_in_system.remove(i)

    def get_free_id(self) -> int:
        if len(self._toys_list_in_system) == 0:
            return 1
        else:
            return len(self._toys_list_in_system) + 1

    def get_toys_list_in_system(self) -> list[Toys]:
        return self._toys_list_in_system
