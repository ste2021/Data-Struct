class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elem):
        node = Node(elem)
        if self.last:
            self.last.next = node
        else:
            self.first = node

        self.last = node
        self._size += 1

        return

    def pop(self):
        if self.first is None:
            return None

            elem = self.first.data
            self.first = self.first.next

            if self.first is None:
                self.last = None

            self._size -= 1
            return elem

    def top(self):
        return self.first.data

    def empty(self):
        return self.first.next

    def __repr__(self):
        r = ''
        pointer = self.first
        while pointer:
            r += '' if r else '['
            r += str(pointer.data)
            pointer = pointer.next
            r += ', ' if pointer else ']'
        return r
