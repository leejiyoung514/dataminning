import pandas as pd
from scipy import stats
from numpy import mean

data1=[4,6,17,16,8,9]
data2=[10,10,10,10,10,10]
chis=stats.chisquare(data1,data2)
print(chis)