import numpy as np
from scipy import stats

np.random.seed(1)
group1=[170+np.random.normal(0,5) for a in range(20)]
group2=[175+np.random.normal(0,10) for a in range(20)]
result1=stats.ttest_ind(group1,group2)
print("검정통계량: %.3f, p-value: %.3f." % result1)
result2=stats.ttest_ind(group1,group2, equal_var=False)
print("검정통계량: %.3f, p-value: %.3f." % result2)