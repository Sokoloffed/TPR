import numpy as np
Grades = [[5, 3, 1, 2, 8, 4, 6, 7],
          [5, 4, 3, 1, 8, 2, 6, 7],
          [1, 7, 5, 4, 8, 2, 3, 6],
          [6, 4, 2.5, 2.5, 8, 1, 7, 5],
          [8, 2, 4, 6, 3, 5, 1, 7],
          [5, 6, 4, 3, 2, 1, 7, 8],
          [2.5, 4, 1, 2.5, 7, 5, 7, 7],
          [2, 4, 1, 3, 4, 5, 8, 7],
          [4, 2, 3, 1, 6, 8, 7, 5],
          [1, 6, 5, 4, 3, 8, 2, 7]]
projects = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З"]


def list_of_tuples(l1, l2):
    return list(map(lambda x, y: (x, y), l1, l2))
def arrays_from_lis(l):
   res1, res2 = [i for i, j in l], [j for i, j in l]
   return res1, res2


means = np.mean(Grades, axis=0)
print("Середні значення", means)
rangeMean = list_of_tuples(means, projects)
rangeMean.sort(key=lambda tup: tup[0])
print("Загальне впорядкування за середніми арифметичними рангів\n", rangeMean)

medians = np.median(Grades, axis=0)
print("\nМедіани", medians)
rangeMedian = list_of_tuples(medians, projects)
rangeMedian.sort(key=lambda tup: tup[0])
print("Загальне впорядкування за медіанами рангів\n",rangeMedian)

num, ranging = arrays_from_lis(rangeMedian)
print("\nУзгоджене ранжування\n", ranging)
print("Ядро суперечностей порожнє\n")


def matrix_distance(l):
    matrix = np.zeros((8,8))
    for i in range (0,8):
        for j in range (0,8):
            if(l[i]>l[j]): matrix[i][j] = 1.
            elif (l[i] < l[j]): matrix[i][j] = -1.
    return matrix


distances = np.empty((10, 10))
for i in range (0,10):
    for j in range (0,10):
        d1 = matrix_distance(Grades[i])
        d2 = matrix_distance(Grades[j])
        t = np.absolute(d1-d2)
        distances[i][j] = 0.5*t.sum()
print("Матриця відстаней Кемені\n",distances)

medianKS = np.argmin(np.sum(distances,axis=1))
print("Медіана Кемені - Снелла", medianKS)
print(Grades[medianKS])