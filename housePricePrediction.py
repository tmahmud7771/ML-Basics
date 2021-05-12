from os import pardir, sep
from pandas.core.algorithms import mode
import sklearn
from  sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#data laod
data = pd.read_csv('Datasets\houses_to_rent.csv', sep=',')
data = data[['id','area','rooms','bathroom','animal','furniture','fire insurance','rent amount']]

#data process 
data['rent amount'] = data['rent amount'].map(lambda i: int(i[2:].replace(',','')))
data['fire insurance'] = data['fire insurance'].map(lambda i: int(i[2:].replace(',','')))
#optiont to digit 
le = preprocessing.LabelEncoder()
data['furniture'] = le.fit_transform(data['furniture'])
data['animal'] =  le.fit_transform(data['animal'])

print(data.head())