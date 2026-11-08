class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        if root is None:
            return Node(value)
        if value < root.value:
            root.left = self._insert(root.left, value)
        elif value > root.value:
            root.right = self._insert(root.right, value)
        return root


    def search(self, root, key):
        if root is None or root.value == key:
            return root
        if key < root.value:
            return self.search(root.left, key)
        return self.search(root.right, key)


    def post_traversal(self, start, traversal):
        if start:
            traversal = self.post_traversal(start.left, traversal)
            traversal = self.post_traversal(start.right, traversal)
            traversal += str(start.value) + "-"
        return traversal


    def delete_node(self, root, key):
        if root is None:    
            return root

        if key < root.value:
            root.left = self.delete_node(root.left, key)
        elif key > root.value:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:  
                return root.left

            successor = root.right
            while successor.left:
                successor = successor.left
            root.value = successor.value
            root.right = self.delete_node(root.right, successor.value)
        return root


#Layout

    def build(self, text):
        numbers = [int(x) for x in text.replace(",", " ").split()]
        self.root = None
        for n in numbers:
            self.insert(n)

    def layout(self):
        nodes, edges, counter = [], [], [0]

        def walk(n, depth):
            if n is None:
                return None
            left = walk(n.left, depth + 1)
            me = {"value": n.value, "x": 30 + counter[0] * 44, "y": 30 + depth * 62}
            counter[0] += 1
            right = walk(n.right, depth + 1)
            nodes.append(me)
            for child in (left, right):
                if child:
                    edges.append((me["x"], me["y"], child["x"], child["y"]))
            return me

        walk(self.root, 0)
        return {
            "nodes": nodes,
            "edges": edges,
            "width": 60 + max(counter[0] - 1, 0) * 44,
            "height": max((n["y"] for n in nodes), default=0) + 30,
        }