from Classes.constraint import Constraint
from Classes.problem import Problem


def ecl_to_array(file_path):
    with open(file_path, 'r') as f:
        problemsECL = f.read()

    resultProblemArray = []

    problemsArray = problemsECL.split(".")
    for index in range(len(problemsArray)):
        resultProblem = []
        problemsArray[index] = "\n".join(problemsArray[index].split("\n")[2:])
        problemsArray[index] = problemsArray[index].replace("[]", "")
        problemsArray[index] = problemsArray[index].replace("(", "")
        problemsArray[index] = problemsArray[index].replace("\n", "")
        problemsArray[index] = problemsArray[index].replace(" ", "")
        problemsArray[index] = problemsArray[index][:len(problemsArray[index])-3]
        problemLines = problemsArray[index].split("),")
        for lineIndex in range(len(problemLines)):
            resultProblem.append(problemLines[lineIndex].split(","))
        resultProblemArray.append(resultProblem)

    return resultProblemArray


def ecl_to_array2(file_path):
    with open(file_path, 'r') as f:
        problemsECL = f.read()

    resultProblemArray = []

    problemsArray = problemsECL.split(".")
    for index in range(len(problemsArray)):
        resultProblem = []
        problemsArray[index] = "\n".join(problemsArray[index].split("\n")[2:])
        problemsArray[index] = problemsArray[index].replace("[]", "")
        problemsArray[index] = problemsArray[index].replace("(", "")
        problemsArray[index] = problemsArray[index].replace("\n", "")
        problemsArray[index] = problemsArray[index].replace(" ", "")
        problemsArray[index] = problemsArray[index][:len(problemsArray[index])-3]
        problemLines = problemsArray[index].split("),")
        for lineIndex in range(len(problemLines)):
            resultProblem.append(problemLines[lineIndex].split(","))
        resultProblemArray.append(resultProblem)

    resultProblemArray.pop()

    for problemIndex in range(len(resultProblemArray)):
        for rowIndex in range(len(resultProblemArray[problemIndex])):
            for cellIndex in range(len(resultProblemArray[problemIndex][rowIndex])):
                if resultProblemArray[problemIndex][rowIndex][cellIndex] == 'x/x':
                    resultProblemArray[problemIndex][rowIndex][cellIndex] = '*'
                elif resultProblemArray[problemIndex][rowIndex][cellIndex] == 'x':
                    resultProblemArray[problemIndex][rowIndex][cellIndex] = '_'
                else:
                    first = resultProblemArray[problemIndex][rowIndex][cellIndex].split('/')[0]
                    second = resultProblemArray[problemIndex][rowIndex][cellIndex].split('/')[1]
                    if first == 'x':
                        first = ''
                    if second == 'x':
                        second = ''
                    resultProblemArray[problemIndex][rowIndex][cellIndex] = [first, second]

    return resultProblemArray


def get_constraints(problem, is_row):
    constraints = []
    for rowIndex in range(len(problem)):
        for cellIndex in range(len(problem[rowIndex])):
            if not isinstance(problem[rowIndex][cellIndex], int):
                if '/' in problem[rowIndex][cellIndex]:
                    if problem[rowIndex][cellIndex].split('/')[is_row] != 'x':
                        total = int(problem[rowIndex][cellIndex].split('/')[is_row])
                        indices = []
                        flag = True
                        for constraintIndicesIndex in range(cellIndex + 1, len(problem[rowIndex])):
                            if isinstance(problem[rowIndex][constraintIndicesIndex], int) and flag:
                                indices.append(int(problem[rowIndex][constraintIndicesIndex]))
                            else:
                                flag = False
                        constraints.append(Constraint(total=total, indices=indices))
    return constraints


def array_to_problem(problem_array):
    resultProblemsArray = []
    for problemIndex in range(len(problem_array)):
        counter = 0
        for rowIndex in range(len(problem_array[problemIndex])):
            for cellIndex in range(len(problem_array[problemIndex][rowIndex])):
                if problem_array[problemIndex][rowIndex][cellIndex] == 'x/x':
                    problem_array[problemIndex][rowIndex][cellIndex] = ''
                if problem_array[problemIndex][rowIndex][cellIndex] == 'x':
                    problem_array[problemIndex][rowIndex][cellIndex] = counter
                    counter = counter + 1
        rowConstraints = get_constraints(problem_array[problemIndex], 1)
        problem_array[problemIndex] = [list(i) for i in zip(*problem_array[problemIndex])]
        colConstraints = get_constraints(problem_array[problemIndex], 0)
        resultProblemsArray.append(Problem(serial_number=problemIndex, length=counter-1, row_constraints=rowConstraints, col_constraints=colConstraints))
    return resultProblemsArray


