from collections import deque


class QueueProcessing:
    def __init__(self):
        self.antrian = deque()

    def enqueue(self, mahasiswa):
        self.antrian.append(mahasiswa)

    def dequeue(self):
        if self.antrian:
            return self.antrian.popleft()
        return None

    def is_empty(self):
        return len(self.antrian) == 0

    def size(self):
        return len(self.antrian)