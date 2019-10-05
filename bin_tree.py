class Tree:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Left: {self.left.value if self.left else 'None'}, Right: {self.right.value if self.right else None}"

    def swap_children(self):
        self.left, self.right = self.right, self.left
        if self.left:
            self.left.swap_children()
        if self.right:
            self.right.swap_children()

    def depth_of_tree(self, leaf):
        if leaf is self:
            return 1
        if self.left:
            left = self.left.depth_of_tree(leaf)
            if left:
                return left
        if self.right:
            right = self.right.depth_of_tree(leaf)
            if right:
                return right
        return None


a = Tree(2)
b = Tree(3)
aa = Tree(5, a, b)

print(aa)
aa.swap_children()

print(aa)

print(aa.depth_of_tree(a))
