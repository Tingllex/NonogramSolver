import nonogramy
import algorytm_genetyczny
import algorytm_PSO


genetyczny = algorytm_genetyczny.Algorytm_genetyczny()
pso = algorytm_PSO.Algorytm_PSO()

nonogramy = nonogramy.nonogramy
fitness = ["fitness_1", "fitness_2", "fitness_3"]


def statystyki_generyczny(nonogram, fitness, ilosc_prob):
    statystyki = []
    for i in range(ilosc_prob):
        statystyki.append(genetyczny.uruchom(nonogram, fitness))
    #print(statystyki)
    sredni_czas = 0
    sredni_wynik = 0
    ukonczony = 0
    for i, j, k in statystyki:
        sredni_czas += i
        sredni_wynik += j
        ukonczony += k
    return "sredni czas: " + str(round(sredni_czas / len(statystyki), 2)), \
           "sredni wynik: " + str(round(sredni_wynik / len(statystyki), 2)), \
           "ilosc ukonczonych: " + str(ukonczony)


def statystyki_pso(nonogram, fitness, ilosc_generacji, ilosc_prob):
    statystyki = []
    for i in range(ilosc_prob):
        statystyki.append(pso.uruchom(nonogram, fitness, ilosc_generacji))
    #print(statystyki)
    sredni_czas = 0
    sredni_wynik = 0
    ukonczony = 0
    for i, j, k in statystyki:
        sredni_czas += i
        sredni_wynik += j
        ukonczony += k
    return "sredni czas: " + str(round(sredni_czas / len(statystyki), 2)), \
           "sredni wynik: " + str(round(sredni_wynik / len(statystyki), 2)), \
           "ilosc ukonczonych: " + str(ukonczony)


print(statystyki_generyczny(nonogramy[6], fitness[1], 10))
#print(statystyki_generyczny(nonogramy[9], fitness[2], 20))
'''print(statystyki_pso(nonogramy[9], fitness[2], 10000, 5))
print(statystyki_pso(nonogramy[9], fitness[2], 20000, 5))
print(statystyki_pso(nonogramy[9], fitness[2], 50000, 5))'''

#print(statystyki_generyczny(nonogramy[0], fitness[1], 10))
#print(statystyki_generyczny(nonogramy[0], fitness[2], 10))
'''
print(statystyki_generyczny(nonogramy[1], fitness[0], 10))
print(statystyki_generyczny(nonogramy[1], fitness[1], 10))
print(statystyki_generyczny(nonogramy[1], fitness[2], 10))

print(statystyki_generyczny(nonogramy[2], fitness[0], 10))
print(statystyki_generyczny(nonogramy[2], fitness[1], 10))
print(statystyki_generyczny(nonogramy[2], fitness[2], 10))

print(statystyki_generyczny(nonogramy[3], fitness[0], 10))
print(statystyki_generyczny(nonogramy[3], fitness[1], 10))
print(statystyki_generyczny(nonogramy[3], fitness[2], 10))

print(statystyki_generyczny(nonogramy[4], fitness[0], 10))
print(statystyki_generyczny(nonogramy[4], fitness[1], 10))
print(statystyki_generyczny(nonogramy[4], fitness[2], 10))

print(statystyki_generyczny(nonogramy[5], fitness[0], 10))
print(statystyki_generyczny(nonogramy[5], fitness[1], 10))
print(statystyki_generyczny(nonogramy[5], fitness[2], 10))

print(statystyki_generyczny(nonogramy[6], fitness[0], 10))
print(statystyki_generyczny(nonogramy[6], fitness[1], 10))
print(statystyki_generyczny(nonogramy[6], fitness[2], 10))

print(statystyki_generyczny(nonogramy[7], fitness[0], 10))
print(statystyki_generyczny(nonogramy[7], fitness[1], 10))
print(statystyki_generyczny(nonogramy[7], fitness[2], 10))

print(statystyki_generyczny(nonogramy[8], fitness[0], 10))
print(statystyki_generyczny(nonogramy[8], fitness[1], 10))
print(statystyki_generyczny(nonogramy[8], fitness[2], 10))
'''
#print(statystyki_generyczny(nonogramy[9], fitness[0], 10))
#print(statystyki_generyczny(nonogramy[9], fitness[1], 10))
#print(statystyki_generyczny(nonogramy[9], fitness[2], 10))

'''
print(statystyki_pso(nonogramy[0], fitness[0], 1000, 10))
print(statystyki_pso(nonogramy[0], fitness[1], 1000, 10))
print(statystyki_pso(nonogramy[0], fitness[2], 1000, 10))

print(statystyki_pso(nonogramy[1], fitness[0], 1000, 10))
print(statystyki_pso(nonogramy[1], fitness[1], 1000, 10))
print(statystyki_pso(nonogramy[1], fitness[2], 1000, 10))

print(statystyki_pso(nonogramy[2], fitness[0], 1000, 10))
print(statystyki_pso(nonogramy[2], fitness[1], 1000, 10))
print(statystyki_pso(nonogramy[2], fitness[2], 1000, 10))'''