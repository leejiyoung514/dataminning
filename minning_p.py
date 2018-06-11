import numpy as np
from scipy import stats

np.random.seed(1)
heights=[180+np.random.normal(0,5) for a in range(20)]
result=stats.ttest_1samp(heights,175)
print("검정통계량: %.3f, p-value: %.3f" % result)
