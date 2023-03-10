class Nonogram:
    def __init__(self, columns, rows, expected_solution):
        self.columns = columns
        self.rows = rows
        self.expected_solution = expected_solution


nonogram_3x3_1 = Nonogram([[1, 1], [2], [1, 1]],
                          [[1, 1], [1], [3]],
                          [[1, 0, 1],
                           [0, 1, 0],
                           [1, 1, 1]])

nonogram_3x3_2 = Nonogram([[3], [1], [3]],
                          [[1, 1], [3], [1, 1]],
                          [[1, 0, 1],
                           [1, 1, 1],
                           [1, 0, 1]])

nonogram_4x4_1 = Nonogram([[1], [2], [3], [1]],
                          [[2], [1], [3], [1]],
                          [[0, 0, 1, 1], [0, 0, 1, 0], [1, 1, 1, 0], [0, 1, 0, 0]])

nonogram_4x4_2 = Nonogram([[1], [1, 1], [4], [1]],
                          [[2], [1], [4], [1]],
                          [[0, 1, 1, 0], [0, 0, 1, 0], [1, 1, 1, 1], [0, 0, 1, 0]])

nonogram_5x5_1 = Nonogram([[1], [2], [2, 1], [4], [3]],
                          [[1], [2], [2], [4], [2, 2]],
                          [[0, 0, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [1, 1, 0, 1, 1]])

nonogram_5x5_2 = Nonogram([[1, 1, 1], [1, 1], [1, 1, 1], [1, 1], [1, 1, 1]],
                          [[1, 1, 1], [1, 1], [1, 1, 1], [1, 1], [1, 1, 1]],
                          [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]])

nonogram_6x6_1 = Nonogram([[1, 2], [3, 1], [1], [3], [3], [1, 2]],
                          [[3, 2], [1, 1], [2, 1], [1, 1], [1, 1], [1, 1, 1]],
                          [[1, 1, 1, 0, 1, 1],
                           [0, 1, 0, 0, 1, 0],
                           [1, 1, 0, 0, 1, 0],
                           [1, 0, 0, 1, 0, 0],
                           [0, 0, 0, 1, 0, 1],
                           [0, 1, 0, 1, 0, 1]])

nonogram_6x6_2 = Nonogram([[2, 1], [1, 2], [2], [1, 1], [2, 1], [2, 2]],
                          [[1, 2, 1], [2, 1, 2], [1, 2, 1], [1, 1, 1], [2, 1, 2], [1, 1, 2]],
                          [[1, 1, 0, 1, 1, 0],
                           [1, 0, 1, 0, 0, 1],
                           [0, 0, 1, 1, 1, 0],
                           [1, 1, 0, 0, 0, 1],
                           [0, 1, 1, 0, 1, 1],
                           [1, 0, 0, 1, 1, 1]])

nonogram_10x10_1 = Nonogram([[1, 2, 1], [3, 1, 2], [1, 2], [3, 1], [3, 2], [1, 2, 1], [2, 1], [3, 1], [1, 2], [1]],
                            [[3, 2, 1], [1, 1, 2], [2, 1, 1], [1, 1, 2], [1, 1, 2], [1, 1, 1, 1], [1, 2, 1], [1, 1],
                             [1, 2], [1]],
                            [[1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
                             [0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
                             [1, 1, 0, 0, 1, 0, 1, 0, 1, 0],
                             [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                             [0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
                             [0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
                             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                             [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                             [0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
                             [0, 1, 0, 1, 0, 1, 1, 0, 1, 1]])

nonogram_15x15_1 = Nonogram([[1, 2, 1, 3], [3, 1, 2, 1], [1, 2, 1, 1], [3, 1, 2, 1], [3, 2, 1, 2],
                             [1, 2, 1, 3], [2, 1, 3, 1], [3, 1, 2, 1], [1, 2, 1, 1], [3, 1, 2, 1],
                             [3, 2, 1, 2], [1, 2, 1, 3], [2, 1, 3, 1], [3, 1, 2, 1], [1, 2, 1]],
                            [[3, 2, 1, 2], [1, 1, 2, 1], [2, 1, 1, 2], [1, 1, 2, 1], [1, 1, 2, 1],
                             [1, 1, 1, 1, 1], [1, 2, 1, 2], [1, 1, 3, 1], [1, 2, 1, 2], [1, 1, 3, 1],
                             [1, 2, 1, 2], [1, 1, 3, 1], [1, 2, 1, 2], [1, 1, 3, 1], [1, 2, 1]],
                            [[1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
                             [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                             [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
                             [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                             [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
                             [0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
                             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                             [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                             [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
                             [0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
                             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                             [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                             [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
                             [0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
                             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

nonogramy = [nonogram_3x3_1, nonogram_3x3_2,
             nonogram_4x4_1, nonogram_4x4_2,
             nonogram_5x5_1, nonogram_5x5_2,
             nonogram_6x6_1, nonogram_6x6_2,
             nonogram_10x10_1, nonogram_15x15_1,
             ]
