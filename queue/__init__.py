class queue():
    li = []
    def queue(self, e):
        self.li.append(e)
        return self

    def dequeue(self):
        return self.li.pop(0)
