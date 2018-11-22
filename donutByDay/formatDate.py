import datetime
import pandas as pd

dataSet = 'trainingSetDono.csv'

df = pd.read_csv(dataSet, sep=',',header=None)
print(df.value)
