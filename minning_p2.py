import numpy as np
from scipy import stats

before=[60+np.random.normal(0,5) for a in range(20)]
after=[w*np.random.normal(0.99,0.02) for w in before]
result=stats.ttest_rel(before,after)
print(result)
