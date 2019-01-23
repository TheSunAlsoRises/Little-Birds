import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   #Data visualisation libraries
import seaborn as sns
import csv
#matplotlib inline

file = csv.reader(open('C://Users\אליה\PycharmProjects\ex.csv'))

for row in file:
    print(row)
    break

df = pd.read_csv(file, sep=';')

