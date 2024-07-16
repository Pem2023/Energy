import pandas as pd

a = pd.read_csv('C:/Users/Nah/Desktop/TESF/ENERGY-Lab/GitHub/2450MHz/00cm0MHz2450010k.csv',usecols=[0,1])

a = a.drop([0,1,2]) 
print(a)