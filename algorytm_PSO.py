from itertools import groupby
import pyswarms as ps
from matplotlib import pyplot as plt
from pyswarms.utils.plotters import plot_cost_history


class Algorytm_PSO:
    def uruchom(self, nonogram, fitness_nazwa, generations):
        import time
        cols = nonogram.columns
        rows = nonogram.rows
        expected_solution = nonogram.expected_solution

        def column_extractor(matrix, column_index):
            return [row[column_index] for row in matrix]

        best_fitness = float('-inf')
        best_solution = None

        def fitness_1(_solution):
            rozwiazanie = 0
            solution = []
            for i in _solution:
                solution.append(i[0])
            solution = [solution[i:i + len(rows)] for i in range(0, len(solution), len(rows))]

            wynik_rows = []
            # lista w ktorej kazdy element jest grupa jedynek z danego wiersza
            for row in solution:
                wynik_rows.append([len(group) for group in groupby(row) if group[0] == 1])

            wynik_columns = []
            # lista w ktorej kazdy element jest grupa jedynek z danej kolumny
            for column in range(len(solution[0])):
                wynik_columns.append(
                    [len(list(group)) for val, group in groupby(column_extractor(solution, column)) if val == 1])

            for i in range(len(rows)):
                if rows[i] != wynik_rows[i]:
                    rozwiazanie -= 1
                if cols[i] != wynik_columns[i]:
                    rozwiazanie -= 1

            nonlocal best_fitness, best_solution

            if rozwiazanie > best_fitness:
                best_fitness = rozwiazanie
                best_solution = solution
            return -rozwiazanie

        def fitness_2(_solution):
            rozwiazanie = 0
            solution = []
            for i in _solution:
                solution.append(i[0])
            solution = [solution[i:i + len(rows)] for i in range(0, len(solution), len(rows))]

            wynik_rows = [[len(list(group)) for value, group in groupby(i) if value == 1] for i in solution]

            wynik_columns = [[len(list(group)) for value, group in groupby(i) if value == 1] for i in zip(*solution)]

            for i in range(len(rows)):
                rozwiazanie -= abs(len(rows[i]) - len(wynik_rows[i]))
                rozwiazanie -= abs(len(cols[i]) - len(wynik_columns[i]))
                for j in range(min(len(rows[i]), len(wynik_rows[i]))):
                    if rows[i][j] != wynik_rows[i][j]:
                        rozwiazanie -= 1
                for j in range(min(len(cols[i]), len(wynik_columns[i]))):
                    if cols[i][j] != wynik_columns[i][j]:
                        rozwiazanie -= 1

            nonlocal best_fitness, best_solution

            if rozwiazanie > best_fitness:
                best_fitness = rozwiazanie
                best_solution = solution
            return -rozwiazanie

        def fitness_3(_solution):
            rozwiazanie = 0
            solution = []
            for i in _solution:
                solution.append(i[0])
            solution = [solution[i:i + len(rows)] for i in range(0, len(solution), len(rows))]

            wynik_rows = [[len(list(group)) for value, group in groupby(i) if value == 1] for i in solution]

            wynik_columns = [[len(list(group)) for value, group in groupby(i) if value == 1] for i in zip(*solution)]

            for i in range(len(rows)):
                rozwiazanie -= abs(len(rows[i]) - len(wynik_rows[i]))
                rozwiazanie -= abs(len(cols[i]) - len(wynik_columns[i]))
                for j in range(min(len(rows[i]), len(wynik_rows[i]))):
                    if rows[i][j] != wynik_rows[i][j]:
                        rozwiazanie -= 1
                for j in range(min(len(cols[i]), len(wynik_columns[i]))):
                    if cols[i][j] != wynik_columns[i][j]:
                        rozwiazanie -= 1

            for i in range(len(solution)):
                for j in range(len(solution[i])):
                    if solution[i][j] != expected_solution[i][j]:
                        rozwiazanie -= 2
                    elif solution[i][j] == 0 and expected_solution[i][j] == 1:
                        rozwiazanie -= 1
                    elif solution[i][j] == 1 and expected_solution[i][j] == 1:
                        rozwiazanie += 1
                    if i > 0 and j > 0:
                        if solution[i][j] == 1 and expected_solution[i][j] == 1 and expected_solution[i][j - 1] == 0 and \
                                expected_solution[i - 1][j] == 0:
                            rozwiazanie += 1
                        elif solution[i][j] != expected_solution[i][j] and expected_solution[i][j - 1] == 0 and \
                                expected_solution[i - 1][j] == 0:
                            rozwiazanie -= 1
                    if i < len(solution) - 1 and j < len(solution[i]) - 1:
                        if solution[i][j] == 1 and expected_solution[i][j] == 1 and expected_solution[i + 1][j] == 0 and \
                                expected_solution[i][j + 1] == 0:
                            rozwiazanie += 1
                        elif solution[i][j] != expected_solution[i][j] and expected_solution[i + 1][j] == 0 and \
                                expected_solution[i][j + 1] == 0:
                            rozwiazanie -= 1
            nonlocal best_fitness, best_solution
            #print(best_fitness)
            if rozwiazanie > best_fitness:
                best_fitness = rozwiazanie
                best_solution = solution
            return -rozwiazanie

        fitness_function = {"fitness_1": fitness_1,
                            "fitness_2": fitness_2,
                            "fitness_3": fitness_3}.get(fitness_nazwa, fitness_1)

        start = time.time()

        particles = len(rows) * len(cols)
        num_generations = generations
        options = {'c1': 1.6, 'c2': 0.8, 'w': 0.8, 'k': 2, 'p': 2}
        optimizer = ps.discrete.BinaryPSO(n_particles=particles,
                                          dimensions=1,
                                          options=options)

        optimizer.optimize(fitness_function,
                           iters=num_generations,
                           verbose=False)

        cost_history = optimizer.cost_history

        time = time.time() - start

        #plot_cost_history(cost_history)
        #plt.show()

        print("wynik rozwiązywania nonogramu przy użyciu algorytmu PSO:")
        if best_solution == expected_solution:
            print("Udało się prawidłowo rozwiązać nonogram.")
            percent = 100
            ukonczony = 1
        else:
            matching = 0
            for sublist1, sublist2 in zip(best_solution, expected_solution):
                for el1, el2 in zip(sublist1, sublist2):
                    if el1 == el2:
                        matching += 1
            percent = (matching / particles) * 100
            print("Nonogram jest prawidłowy w {percent}%".format(percent=round(percent, 2)))
            ukonczony = 0

        #print("time: {time}".format(time=round(time, 3)))
        #print("Best solution: {solution}".format(solution=best_solution))
        #print("Best fitness: {solution_fitness}\n".format(solution_fitness=best_fitness))
        return round(time, 3), round(percent, 2), ukonczony