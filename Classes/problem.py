class Problem:
    def __init__(self, length, row_constraints, col_constraints):
        self.length = length
        self.row_constraints = row_constraints
        self.col_constraints = col_constraints

    def get_solutions_fitness_score(self, solution):
        score = 0
        for constraint in self.row_constraints:
            if constraint.fits(solution):
                score = score + 1
        for constraint in self.col_constraints:
            if constraint.fits(solution):
                score = score + 1
        return score
