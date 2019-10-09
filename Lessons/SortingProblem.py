class Entry:
    def __init__(self, name, id_number, priority):
        self.name = name
        self.id_number= id_number
        self.priority = priority

    def __repr__(self):
        return f"{self.id_number}-{self.name}-{self.priority}"


lst = [
    Entry("first", 4, 2),
    Entry("second", 2, 5),
    Entry("third", 7, 2),
    Entry("fourth", 12, 9)
]

print(f"By ID: {sorted(lst, key=lambda entry: entry.id_number)}")
print(f"By name: {sorted(lst, key=lambda entry: entry.name)}")
print(f"By priority: {sorted(lst, key=lambda entry: entry.priority)}")
