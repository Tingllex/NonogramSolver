from itertools import groupby
import pygad


class Algorytm_genetyczny:
    def uruchom(self, nonogram, fitness_nazwa):
        import time
        cols = nonogram.columns
        rows = nonogram.rows
        expected_solution = nonogram.expected_solution

        gene_space = [0, 1]

        def column_extractor(matrix, column_index):
            return [row[column_index] for row in matrix]

        # definiujemy funkcję fitness
        def fitness_1(solution, solution_idx):
            rozwiazanie = 0
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
            return rozwiazanie

        def fitness_2(solution, solution_idx):
            rozwiazanie = 0
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

            return rozwiazanie

        def fitness_3(solution, solution_idx):
            rozwiazanie = 0
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
                        if solution[i][j] == 1 and expected_solution[i][j] == 1 and expected_solution[i][j - 1] == 0 and expected_solution[i - 1][j] == 0:
                            rozwiazanie += 1
                        elif solution[i][j] != expected_solution[i][j] and expected_solution[i][j - 1] == 0 and expected_solution[i - 1][j] == 0:
                            rozwiazanie -= 1
                    if i < len(solution) - 1 and j < len(solution[i]) - 1:
                        if solution[i][j] == 1 and expected_solution[i][j] == 1 and expected_solution[i + 1][j] == 0 and expected_solution[i][j + 1] == 0:
                            rozwiazanie += 1
                        elif solution[i][j] != expected_solution[i][j] and expected_solution[i + 1][j] == 0 and expected_solution[i][j + 1] == 0:
                            rozwiazanie -= 1


            return rozwiazanie

        fitness_function = {"fitness_1": fitness_1,
                            "fitness_2": fitness_2,
                            "fitness_3": fitness_3}.get(fitness_nazwa, fitness_1)

        # ile chromsomów w populacji
        # ile genow ma chromosom
        sol_per_pop = 100
        num_genes = len(rows) * len(cols)

        # ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
        # ile pokolen
        # ilu rodzicow zachowac (kilka procent)
        num_parents_mating = 50
        num_generations = 100
        keep_parents = 2

        parent_selection_type = "sss"

        crossover_type = "single_point"

        mutation_type = "random"
        mutation_percent_genes = 12

        # inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
        start = time.time()
        ga_instance = pygad.GA(gene_space=gene_space,
                               num_generations=num_generations,
                               num_parents_mating=num_parents_mating,
                               fitness_func=fitness_function,
                               sol_per_pop=sol_per_pop,
                               num_genes=num_genes,
                               parent_selection_type=parent_selection_type,
                               keep_parents=keep_parents,
                               crossover_type=crossover_type,
                               mutation_type=mutation_type,
                               mutation_percent_genes=mutation_percent_genes)

        # uruchomienie algorytmu
        ga_instance.run()

        time = time.time() - start

        solution, solution_fitness, solution_idx = ga_instance.best_solution()
        solution = [solution[i:i + len(rows)] for i in range(0, len(solution), len(rows))]
        solution = [i.tolist() for i in solution]
        print("wynik rozwiązywania nonogramu przy użyciu algorytmu genetycznego:")
        if solution == expected_solution:
            print("Udało się prawidłowo rozwiązać nonogram.")
            percent = 100
            ukonczony = 1
        else:
            matching = 0
            for sublist1, sublist2 in zip(solution, expected_solution):
                for el1, el2 in zip(sublist1, sublist2):
                    if el1 == el2:
                        matching += 1
            percent = (matching / num_genes) * 100
            print("Nonogram jest prawidłowy w {percent}%".format(percent=round(percent, 2)))
            ukonczony = 0

        #print("time: {time}".format(time=round(time, 3)))
        #print("Best solution: {solution}".format(solution=solution))
        #print("Best fitness: {solution_fitness}\n".format(solution_fitness=0))
        return round(time, 3), round(percent, 2), ukonczony
