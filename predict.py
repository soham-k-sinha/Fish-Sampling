import pandas as pd
import math


K = 4

df = pd.read_csv('fish_data.csv')
df = df.sample(frac = 1)

tr = int(len(df) * 0.7)
te = int(len(df) * 0.3)

df_train = df.iloc[:tr, :]
df_test = df.iloc[tr:, :]


all_species = list(df_train.species.unique())


def distance(length1, weight1, ratio1, ind2):
    return math.sqrt((length1 - df_train.iloc[ind2].length)**2 + (weight1 - df_train.iloc[ind2].weight)**2 + (ratio1 - df_train.iloc[ind2].w_l_ratio)**2)



def point(length, weight, ratio):
    distances = {}
    for i in range(len(df_train)):
        distances.update({i: distance(length, weight, ratio, i)})

    sort = list(dict(sorted(distances.items(), key=lambda item: item[1])).items())
    
    neighbours = sort[:K]
    species = []

    for i in neighbours:
        species.append(df_train.iloc[i[0]].species)        

    
    count = {k:species.count(k) for k in species}
    count_sort = list(dict(sorted(count.items(), key=lambda item: item[1])).items())
    return count_sort[0][0]


def testing():
    spec = []
    for i in range(len(df_test)):
        a = point(df_test.iloc[i].length, df_test.iloc[i].weight, df_test.iloc[i].w_l_ratio)
        spec.append(a == df_test.iloc[i].species)
    
    b = str((spec.count(True)/len(spec)) * 100) + " % Accuracy"
    return b

accuracy = testing()
print(accuracy)

