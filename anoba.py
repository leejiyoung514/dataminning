import matplotlib.pyplot as plt
import scipy.stats as stats

a=[66,74,82,75,73,97,87,78]
b=[72,51,59,62,74,64,78,63]
c=[61,60,57,60,81,55,70,71]
d=[63,61,76,84,58,65,69,80]

plot_data=[a,b,c,d]
ax=plt.boxplot(plot_data)
plt.show()
F_statistic, pVal=stats.f_oneway(a,b,c,d)
print('F={0:.1f},p={1:.3f}'.format(F_statistic, pVal))
