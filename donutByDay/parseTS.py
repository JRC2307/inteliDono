import csv
import pandas as pd
import numpy as np

dataSet = 'trainingSetDono.csv'
trainData = []
uniqueDates = []
donaKind = ['PL', 'XC', 'VL', 'CI', 'MT', 'CT', 'NV', 'RM', 'NT', 'TC', 'CH', 'CK', 'RC', 'HM', 'PT', 'MC', 'CJ']
outData = []

with open(dataSet, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        trainData.append(row)
        if row[0] not in uniqueDates:
            uniqueDates.append(row[0])

    for u in uniqueDates:
        dateArray = u.split('/')
        data = [dateArray[0],dateArray[1],dateArray[2], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for t in trainData:
            if t[0] == u:
                if t[1] == 'PL':
                    data[3] = data[3] + 1
                elif t[1] == 'XC':
                    data[4] = data[4] + 1
                elif t[1] == 'VL':
                    data[5] = data[5] + 1
                elif t[1] == 'CI':
                    data[6] = data[6] + 1
                elif t[1] == 'MT':
                    data[7] = data[7] + 1
                elif t[1] == 'CT':
                    data[8] = data[8] + 1
                elif t[1] == 'NV':
                    data[9] = data[9] + 1
                elif t[1] == 'RM':
                    data[10] = data[10] + 1
                elif t[1] == 'NT':
                    data[11] = data[11] + 1
                elif t[1] == 'TC':
                    data[12] = data[12] + 1
                elif t[1] == 'CH':
                    data[13] = data[13] + 1
                elif t[1] == 'CK':
                    data[14] = data[14] + 1
                elif t[1] == 'RC':
                    data[15] = data[15] + 1
                elif t[1] == 'HM':
                    data[16] = data[16] + 1
                elif t[1] == 'PT':
                    data[17] = data[17] + 1
                elif t[1] == 'MC':
                    data[18] = data[18] + 1
                elif t[1] == 'CJ':
                    data[19] = data[19] + 1
        outData.append(data)

    print(outData)
    a = np.array(outData)
    df = pd.DataFrame(a)
    df.to_csv("labuena.csv")

    print(a)
# def getData():
# count = 0
# retrieve data from file
# data = pd.read_csv(dataSet, sep=',',header=None)
# data.values

# for i in data:
#    prod = data.values[i][1]
#    type = data.values[i][2]
#    #Parse donas to 1 other products 0
#    if "Donas" not in prod:
#        prod = 0
#    else:
#        prod = 1
#
#    #Parse donut types
#    if "Dona Cookies &Cream" in type:
#        type = 0
#    elif "Dona Nutella" in type:
#        type = 1
#    elif "Dona de Menta" in type:
#        type = 2
#    elif "Dona de chocolate" in type:
#        type = 3
#    elif "Dona Espolvoreada" in type:
#        type = 4
#    elif "Dona maple con tocino" in type:
#        type = 5
#    elif "Dona Pie de Limon" in type:
#        type = 6
#    elif "Dona Crema Irlandesa" in type:
#        type = 7
#    print("product " + str(prod) + " type: " + str(type))


#    pass
