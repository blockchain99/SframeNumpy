import pandas as pd
import numpy as np

def add_number(num_l):
    num_list = []
    pd_s = pd.Series([1,2,3,4])
    for ele in num_l:
        num_list.append(ele)
    pd_new = pd.Series(num_list)
    result = pd_s + pd_new
    return result

a=[4,5,6,7]
result = add_number(a)
print result