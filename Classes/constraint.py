class Constraint:
    def __init__(self, total, indices):
        self.total = total
        self.indices = indices

    def fits(self, solution):
        counter = 0
        for index in self.indices:
            counter = counter + solution[index]
        return counter == self.total
