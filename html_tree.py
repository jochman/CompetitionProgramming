class HTML:
    inbound = list()
    outbound = list()

    def __init__(self, data):
        assert data is not None
        self.data = data

    def __repr__(self):
        return f"{self.data}"


def build_tree(left_roots: int, root: HTML):
    new_left = left_roots - len(root.objects)
    if new_left is 0:
        return root.name
    elif new_left < 0:
        return None
    else:
        lst = [x.name for x in root.objects if build_tree(new_left - 1, x) is not None]
        if lst:
            return f"{root.name} {lst[0]}"
        else:
            return None


aa = HTML("s.com", [])
a = HTML("one.co.il", [aa])
b = HTML("nba.com", [a, aa])
c = HTML("y", [a, b])
tree = build_tree(5, c)
print(tree)
