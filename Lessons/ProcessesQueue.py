from queue import PriorityQueue
from typing import Any, List


class Process:
    def __new__(cls, *args, **kwargs):
        if "t" in kwargs:
            t = kwargs["t"]
        else:
            t = args[3]
        t < t
        t > t
        t == t
        return super(Process, cls).__new__(cls)

    def __init__(self, name: str, priority: int, processes: List, t: Any):
        self.processes = processes
        self.priority = priority
        self.name = name
        self.t = t

    def __repr__(self):
        return f"{self.priority}. {self.name}: {self.processes}, {self.t}"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        if self.priority == other.priority:
            return self.t == other.t
        return True

    def __lt__(self, other):
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __gt__(self, other):
        return self.priority < other.priority

    def __ge__(self, other):
        return self.priority <= other.priority


class ProcessesQueue(PriorityQueue):
    def __init__(self, maxsize=0):
        super().__init__(maxsize)

    def put(self, item: Process, **kwargs) -> None:
        super().put((item.priority, item), **kwargs)

    def get(self, **kwargs) -> Process:
        return super().get()[1]

    def __repr__(self):
        f = str()
        new_q = self
        while not new_q.empty():
            e = new_q.get()
            f += f"{{{str(e)}}}\n"
        return f


if __name__ == '__main__':
    q = ProcessesQueue()
    p_lst = [
        Process("first", 3, [], 2),
        Process("sec", 2, [], 7),
        Process("third", 1, [], 3)
    ]
    for p in p_lst:
        q.put(p)

    print(q)
