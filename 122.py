from collections import defaultdict

class Node:
    __slots__ = ['parent', 'children', 'value']
    def __init__(self, value, parent=None, children=None):
        self.value = value
        self.children = children or []
        self.parent = parent

    def add_child(self, node):
        if node.__class__.__name__ == 'int':
            node = Node(node)
        node.parent = self
        self.children.append(node)

    def add_parent(self, node):
        node.children.append(self)
        self.parent = node

    def remove(self):
        self.parent = None
        self.children = []

    def get_path(self):
        path = []
        node = self
        while node:
            path.append(node.value)
            node = node.parent
        return path

class Tree:
    __slots__ = ['level_map']
    def __init__(self, root=None):
        self.level_map = defaultdict(list)
        if root: self.add(root, 0)

    def add(self, node, depth):
        self.level_map[depth].append(node)

    def trim(self, condition=None):
        default = lambda x: True
        condition = condition or default
        max_depth = max(self.level_map.keys())
        leaves = self.level_map[max_depth]
        seen = { node.value for depth, node in self.level_map.items() for node in node if depth < max_depth }
        new_leaves = []
        for leaf in leaves:
            if leaf.value not in seen and condition(leaf.value):
                new_leaves.append(leaf)
            else:
                leaf.remove()
        self.level_map[max_depth] = new_leaves

    def grow(self):
        max_depth = max(self.level_map.keys())
        leaves = self.level_map[max_depth]
        for leaf in leaves:
            for n in reversed(leaf.get_path()):
                node = Node(leaf.value + n, leaf)
                self.add(node, max_depth+1)

    def find(self, target):
        for level in sorted(self.level_map.keys()):
            for node in self.level_map[level]:
                if node.value == target: return level

def run(n):
    t = Tree(Node(1))
    def check():
        result = 0
        for i in range(2, n+1):
            x = t.find(i)
            if x:
                result += x
            else:
                break
        else:
            return result
        t.grow()
        t.trim(lambda x: x <= n)
        return check()
    return check()

def bm(n):
    from time import time
    t0 = time()
    run(n)
    t1 = time()
    print(t1-t0)
