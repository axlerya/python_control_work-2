class Toys:

    def __init__(self, id: int, name: str, count: int, priority: int):
        self._id = id
        self._name = name
        self._count = count
        self._priority = priority

    def reduce_count(self, x: int) -> int:
        self._count -= x

    def add_count(self, x: int) -> int:
        self._count += x

    def edit_priority(self, priority: int):
        self._priority = priority

    def __repr__(self) -> str:
        return f"{self._name}\nid = {self._id}\n"
    
    def __str__(self) -> str:
        return f"{self._name}\nid = {self._id}\n"
    
