import pandas as pd

dataSet = 'trainingSetDono.csv'

def getData():
    count = 0
    #retrieve data from file
    data = pd.read_csv(dataSet, sep=',',header=None)
    data.values

    for i in data:
        prod = data.values[i][1]
        type = data.values[i][2]
        #Parse donas to 1 other products 0
        if "Donas" not in prod:
            prod = 0
        else:
            prod = 1

        #Parse donut types
        if "Dona Cookies &Cream" in type:
            type = 0
        elif "Dona Nutella" in type:
            type = 1
        elif "Dona de Menta" in type:
            type = 2
        elif "Dona de chocolate" in type:
            type = 3
        elif "Dona Espolvoreada" in type:
            type = 4
        elif "Dona maple con tocino" in type:
            type = 5
        elif "Dona Pie de Limon" in type:
            type = 6
        elif "Dona Crema Irlandesa" in type:
            type = 7
        print("product " + str(prod) + " type: " + str(type))


    pass
