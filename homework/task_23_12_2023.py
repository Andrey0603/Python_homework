
import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

unique_labels = list(set(lst))  
one_hot_encoding = []
for item in lst:
    encoding = [1 if item == label else 0 for label in unique_labels]
    one_hot_encoding.append(encoding)

one_hot_df = pd.DataFrame(one_hot_encoding, columns=unique_labels)
one_hot_df.head()