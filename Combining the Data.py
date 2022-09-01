import pandas as pd
import numpy as np

df_list = []
#path =/Users/admin/Desktop/Aparna Project Final Individual Data/S2.csv
l = [2,3,4,5,6,7,8,9,10,11,13,14,15,16,17]
for i in l :
    path = '/Users/admin/Desktop/Datast with window size 1 and no chest eda temp etc./S' + str(i) + '.csv'
    df = pd.read_csv(path)
    df_list.append(df)

df = pd.concat(df_list)
print(df.shape)
df.reset_index(inplace=True)
miss_values = np.isnan(df).values.sum()
print(miss_values) 
df.to_csv(r'/Users/admin/Desktop/Datast with window size 1 and no chest eda temp etc./Final Dataset/Data.csv', index = False)

