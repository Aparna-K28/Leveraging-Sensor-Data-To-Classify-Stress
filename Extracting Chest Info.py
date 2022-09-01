from statistics import mean
from joblib import dump,load
import pickle
import pandas as pd

path = 'Enter Path Name'
d = pd.read_pickle(path)
df = pd.DataFrame()
Labels = list(d['label'])
def looping(a, b) :
    l = []
    for i in d['signal'][a][b] :
        l.append(float(i))
    return l

def acc_loop() :
    m1 = []
    m2 = []
    m3 = []
    for i in d['signal']['chest']['ACC'] :
        m1.append(float(i[0]))
        m2.append(float(i[1]))
        m3.append(float(i[2]))
    return m1,m2,m3


C_EDA = looping('chest','EDA')
C_Temp = looping('chest','Temp')
C_EMG = looping('chest','EMG')
C_Resp = looping('chest','Resp')
C_ECG = looping('chest','ECG')
C_ACC1, C_ACC2, C_ACC3 = acc_loop()

df = df.assign(Chest_ACC1 = C_ACC1)
df = df.assign(Chest_ACC2 = C_ACC2)
df = df.assign(Chest_ACC3 = C_ACC3)
df = df.assign(Chest_EDA = C_EDA)
df = df.assign(Chest_EMG = C_EMG)
df = df.assign(Chest_Temp = C_Temp)
df = df.assign(Chest_Resp = C_Resp)
df = df.assign(Chest_ECG = C_ECG)
df = df.assign(Label = Labels)


df.to_csv(r'Enter Path Name', index = False)
