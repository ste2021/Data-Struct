# Deque - Estrutura
# ------------------------------------------------------
# construtor node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class Deck:
    def __init__(self):
        self.left = None
        self.right = None
        self._size = 0

    def __len__(self):
        return self._size

    def empty(self):
        return self._size == 0
# -------------------------------------------------------
# Inserir Elementos no Deque

    def push_left(self, elem):
        node = Node(elem)

        if self.empty():
            self.left = node
            self.right = node

        else:
            self.left.previous = node
            node.next = self.left
            self.left = node

        self._size += 1

    def push_right(self, elem):
        node = Node(elem)

        if self.empty():
            self.right = node
            self.left = node

        else:
            self.right.next = node
            node.prevous = self.right
            self.right = node

        self._size += 1
# -------------------------------------------------------
# Exibe Elementos no Deque

    def top_left(self):
        if self.left:
            return self.left.data
        return "Deque Vazio"

    def top_right(self):
        if self.right:
            return self.right.data
        return "Deque vazio"
# -------------------------------------------------------
# Exclui Elementos no Deque

    def pop_left(self):
        if self.empty():
            return "Deque Vazio"
        elem = self.left.data
        self.left = self.left.next
        self.left.previous = None
        self._size = 1
        return elem

    def pop_right(self):
        if self.empty():
            return "Deque Vazio"
        elem = self.right.data
        self.right = self.right.previous
        self.right.next = None
        self._size = 1
        return elem

    def __repr__(self):
        r = ''
        pointer = self.left
        while pointer:
            r += '' if r else '['
            r += str(pointer.data)
            pointer = pointer.next
            r += '<->' if pointer else ']'
        return r
