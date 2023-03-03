import numpy as np
import os
import pandas as pd
class_symbols = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"]
file ="diabetes.txt"
objects = np.loadtxt(file, dtype=str)
# print(objects)
decision =np.unique(np.loadtxt(file, dtype=str, usecols=8))
print("decyzje: ", decision)
decision_count_arr = np.loadtxt(file, dtype=int, usecols=8)
decision_1 = np.count_nonzero(decision_count_arr == 1)
decision_0 = np.count_nonzero(decision_count_arr == 0)
print("decision = 1: ", decision_1)
print("decision = 0: ", decision_0)

def getAttributes(col):
    return np.loadtxt(file, dtype=float, usecols=col)


attr1max = np.max(getAttributes(1))
attr1min =np.min(getAttributes(1))

attr2max = np.max(getAttributes(2))
attr2min =np.min(getAttributes(2))

attr3max = np.max(getAttributes(3))
attr3min =np.min(getAttributes(3))

attr4max = np.max(getAttributes(4))
attr4min =np.min(getAttributes(4))

attr5max = np.max(getAttributes(5))
attr5min =np.min(getAttributes(5))

attr6max = np.max(getAttributes(6))
attr6min =np.min(getAttributes(6))

attr7max = np.max(getAttributes(7))
attr7min =np.min(getAttributes(7))

attr8max = np.max(getAttributes(8))
attr8min =np.min(getAttributes(8))


attr1values = np.unique(getAttributes(1))
attr2values = np.unique(getAttributes(2))
attr3values = np.unique(getAttributes(3))
attr4values = np.unique(getAttributes(4))
attr5values = np.unique(getAttributes(5))
attr6values = np.unique(getAttributes(6))
attr7values = np.unique(getAttributes(7))
attr8values = np.unique(getAttributes(8))

attr1valuescount = len(attr1values)
attr2valuescount = len(attr2values)
attr3valuescount = len(attr3values)
attr4valuescount = len(attr4values)
attr5valuescount = len(attr5values)
attr6valuescount = len(attr6values)
attr7valuescount = len(attr7values)
attr8valuescount = len(attr8values)

std1 = np.std(attr1values)
std2 = np.std(attr2values)
std3 = np.std(attr3values)
std4 = np.std(attr4values)
std5 = np.std(attr5values)
std6 = np.std(attr6values)
std7 = np.std(attr7values)
std8 = np.std(attr8values)

std0 = np.std(np.loadtxt(file, dtype=float, usecols=(1,8)))





def iterate_and_substitute(random_choicex, attrxvalues):
    for i in random_choicex:
        attrxvalues[i] = "?"
    for j in range(len(attrxvalues)):
        if attrxvalues[j] == "?":
             attrxvalues[j] = np.mean(attrxvalues)


# random_choice1 = np.random.choice(range(len(str(attr1values))), int(0.1*objects.shape[0]), replace=False)
# random_choice2 = np.random.choice(range(len(str(attr2values))), int(0.1*objects.shape[0]), replace=False)
# random_choice3 = np.random.choice(range(len(str(attr3values))), int(0.1*objects.shape[0]), replace=False)
# random_choice4 = np.random.choice(range(len(str(attr4values))), int(0.1*objects.shape[0]), replace=False)
# random_choice5 = np.random.choice(range(len(str(attr5values))), int(0.1*objects.shape[0]), replace=False)
# random_choice6 = np.random.choice(range(len(str(attr6values))), int(0.1*objects.shape[0]), replace=False)
# random_choice7 = np.random.choice(range(len(str(attr7values))), int(0.1*objects.shape[0]), replace=False)
# random_choice8 = np.random.choice(range(len(str(attr8values))), int(0.1*objects.shape[0]), replace=False)

# iterate_and_substitute(random_choice1, attr1values)
# iterate_and_substitute(random_choice2, attr2values)
# iterate_and_substitute(random_choice3, attr3values)
# iterate_and_substitute(random_choice4, attr4values)
# iterate_and_substitute(random_choice5, attr5values)
# iterate_and_substitute(random_choice6, attr6values)
# iterate_and_substitute(random_choice7, attr7values)
# iterate_and_substitute(random_choice8, attr8values)

def normalize(left, right, min, max, attrxvalues):
    normalized = []
    for i in range(len(attrxvalues)):
        normalized[i] = ((attrxvalues[i] - min) * (right - left) / (max - min)) + left


# normalize(-1,1,attr1min, attr1max, attr1values)
# normalize(-1,1,attr2min, attr2max, attr2values)
# normalize(-1,1,attr3min, attr3max, attr3values)
# normalize(-1,1,attr4min, attr4max, attr4values)
# normalize(-1,1,attr5min, attr5max, attr5values)
# normalize(-1,1,attr6min, attr6max, attr6values)
# normalize(-1,1,attr7min, attr7max, attr7values)
# normalize(-1,1,attr8min, attr8max, attr8values)

# normalize(0, 1,attr1min, attr1max, attr1values)
# normalize(0, 1,attr2min, attr2max, attr2values)
# normalize(0, 1,attr3min, attr3max, attr3values)
# normalize(0, 1,attr4min, attr4max, attr4values)
# normalize(0, 1,attr5min, attr5max, attr5values)
# normalize(0, 1,attr6min, attr6max, attr6values)
# normalize(0, 1,attr7min, attr7max, attr7values)
# normalize(0, 1,attr8min, attr8max, attr8values)
#
# normalize(-10, 10,attr1min, attr1max, attr1values)
# normalize(-10, 10,attr2min, attr2max, attr2values)
# normalize(-10, 10,attr3min, attr3max, attr3values)
# normalize(-10, 10,attr4min, attr4max, attr4values)
# normalize(-10, 10,attr5min, attr5max, attr5values)
# normalize(-10, 10,attr6min, attr6max, attr6values)
# normalize(-10, 10,attr7min, attr7max, attr7values)
# normalize(-10, 10,attr8min, attr8max, attr8values)

def mean_var_standard(attrxvalues):
    mean = (sum(attrxvalues) / len(attrxvalues))
    print(mean)
    var_arr = np.empty(shape=attrxvalues.shape)
    standard = np.empty(shape=attrxvalues.shape)
    for i in range(len(attrxvalues)):
        var_arr[i] = pow(attrxvalues[i] - mean, 2)
    var = pow(sum(var_arr), 0.5)
    print(var)
    for i in range(len(attrxvalues)):
        standard[i] = (attrxvalues[i] - mean) / var
    return standard

standard1 = mean_var_standard(attr1values)
standard2 = mean_var_standard(attr2values)
standard3 = mean_var_standard(attr3values)
standard4 = mean_var_standard(attr4values)
standard5 = mean_var_standard(attr5values)
standard6 = mean_var_standard(attr6values)
standard7 = mean_var_standard(attr7values)
standard8 = mean_var_standard(attr8values)


