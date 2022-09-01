from statistics import mean, median
from scipy.stats import iqr
from statistics import stdev
import pandas as pd


path = '#Enter path name'
d = pd.read_pickle(path)

#Lists to extract wrist related information
W_ACC1 = []
W_ACC2 = []
W_ACC3 = []
W_BVP  = []
W_TEMP = []

#Loop to extract ACC values
def acc_loop() :
    m1 = []
    m2 = []
    m3 = []
    for i in d['signal']['wrist']['ACC'] :
        m1.append(float(i[0]))
        m2.append(float(i[1]))
        m3.append(float(i[2]))
    return m1,m2,m3

W_ACC1, W_ACC2, W_ACC3 = acc_loop()

#Loop to extract all other values
def looping(b) :
    l = []
    for i in d['signal']['wrist'][b] :
        l.append(float(i))
    return l

W_BVP = looping('BVP')
W_EDA = looping('EDA')
W_TEMP = looping('TEMP')


df = pd.DataFrame()

#List to store label
l = []

#Lists to store standard deviation values
s_acc1 = []
s_acc2 = []
s_acc3 = []
s_eda = []
s_emg = []
s_temp = []
s_resp = []
s_ecg = []

s_weda = []
s_wtemp = []

s_wacc1 =[]
s_wacc2 = []
s_wacc3 = []
s_wbvp = []

#Lists to store mean values of groups
avg_acc1 = []
avg_acc2 = []
avg_acc3 = []
avg_ecg = []
avg_emg = []
avg_eda = []
avg_resp = []
avg_temp = []

avg_weda = []
avg_wtemp = []

avg_wacc1 =[]
avg_wacc2 = []
avg_wacc3 = []
avg_wbvp = []

#Lists to store min values of groups
mn_acc1 = []
mn_acc2 = []
mn_acc3 = []
mn_ecg = []
mn_emg = []
mn_eda = []
mn_resp = []
mn_temp = []

mn_weda = []
mn_wtemp = []

mn_wacc1 =[]
mn_wacc2 = []
mn_wacc3 = []
mn_wbvp = []

#Lists to store the max value of groups
mx_acc1 = []
mx_acc2 = []
mx_acc3 = []
mx_ecg = []
mx_emg = []
mx_eda = []
mx_resp = []
mx_temp = []

mx_weda = []
mx_wtemp = []

mx_wacc1 =[]
mx_wacc2 = []
mx_wacc3 = []
mx_wbvp = []



dat = pd.read_csv("/Users/admin/Desktop/Data/S17.csv")


for i in range(0, len(dat), 700) :

    #Mean 
    mean_acc1 = mean(dat.Chest_ACC1[i:i+700])
    mean_acc2 = mean(dat.Chest_ACC2[i:i+700])
    mean_acc3 = mean(dat.Chest_ACC3[i:i+700])
    mean_eda = mean(dat.Chest_EDA[i:i+700])
    mean_emg = mean(dat.Chest_EMG[i:i+700])
    mean_temp = mean(dat.Chest_Temp[i:i+700])
    mean_resp = mean(dat.Chest_Resp[i:i+700])
    mean_ecg = mean(dat.Chest_ECG[i:i+700])

    #Standard Deviation
    sd_acc1 = stdev(dat.Chest_ACC1[i:i+700])
    sd_acc2 = stdev(dat.Chest_ACC2[i:i+700])
    sd_acc3 = stdev(dat.Chest_ACC3[i:i+700])
    sd_eda = stdev(dat.Chest_EDA[i:i+700])
    sd_emg = stdev(dat.Chest_EMG[i:i+700])
    sd_temp = stdev(dat.Chest_Temp[i:i+700])
    sd_resp = stdev(dat.Chest_Resp[i:i+700])
    sd_ecg = stdev(dat.Chest_ECG[i:i+700])

    #Minimum values
    min_acc1 = min(dat.Chest_ACC1[i:i+700])
    min_acc2 = min(dat.Chest_ACC2[i:i+700])
    min_acc3 = min(dat.Chest_ACC3[i:i+700])
    min_eda = min(dat.Chest_EDA[i:i+700])
    min_emg = min(dat.Chest_EMG[i:i+700])
    min_temp = min(dat.Chest_Temp[i:i+700])
    min_resp = min(dat.Chest_Resp[i:i+700])
    min_ecg = min(dat.Chest_ECG[i:i+700])

    #Maximum values
    max_acc1 = max(dat.Chest_ACC1[i:i+700])
    max_acc2 = max(dat.Chest_ACC2[i:i+700])
    max_acc3 = max(dat.Chest_ACC3[i:i+700])
    max_eda = max(dat.Chest_EDA[i:i+700])
    max_emg = max(dat.Chest_EMG[i:i+700])
    max_temp = max(dat.Chest_Temp[i:i+700])
    max_resp = max(dat.Chest_Resp[i:i+700])
    max_ecg = max(dat.Chest_ECG[i:i+700])
    
    #Appending standard deviation values to a list
    s_acc1.append(sd_acc1)
    s_acc2.append(sd_acc2)
    s_acc3.append(sd_acc3)
    s_ecg.append(sd_ecg)
    s_emg.append(sd_emg)
    s_eda.append(sd_eda)
    s_resp.append(sd_resp)
    s_temp.append(sd_temp)

    #Appending mean values to a list
    avg_acc1.append(mean_acc1)
    avg_acc2.append(mean_acc2)
    avg_acc3.append(mean_acc3)
    avg_ecg.append(mean_ecg)
    avg_emg.append(mean_emg)
    avg_eda.append(mean_eda)
    avg_resp.append(mean_resp)
    avg_temp.append(mean_temp)

    #Appending min values to a list
    mn_acc1.append(min_acc1)
    mn_acc2.append(min_acc2)
    mn_acc3.append(min_acc3)
    mn_ecg.append(min_ecg)
    mn_emg.append(min_emg)
    mn_eda.append(min_eda)
    mn_resp.append(min_resp)
    mn_temp.append(min_temp)

    #Appending max values to a list
    mx_acc1.append(max_acc1)
    mx_acc2.append(max_acc2)
    mx_acc3.append(max_acc3)
    mx_ecg.append(max_ecg)
    mx_emg.append(max_emg)
    mx_eda.append(max_eda)
    mx_resp.append(max_resp)
    mx_temp.append(max_temp)

    #Extracting the mode of labels
    modelab = int(dat.Label[i:i+700].mode())
    l.append(modelab)

for i in range(0,len(W_ACC1),32) :

    #Extracting mean and appending to a list
    meanwacc1 = mean(W_ACC1[i:i+32])
    meanwacc2 = mean(W_ACC2[i:i+32])
    meanwacc3 = mean(W_ACC3[i:i+32])
    avg_wacc1.append(meanwacc1)
    avg_wacc2.append(meanwacc2)
    avg_wacc3.append(meanwacc3)

    #Extracting standard deviation and appending to a list
    stdwacc1 = stdev(W_ACC1[i:i+32])
    stdwacc2 = stdev(W_ACC2[i:i+32])
    stdwacc3 = stdev(W_ACC3[i:i+32])
    s_wacc1.append(stdwacc1)
    s_wacc2.append(stdwacc2)
    s_wacc3.append(stdwacc3)

    #Extracting minimum values and appending to a list
    min_wacc1 = min(W_ACC1[i:i+32])
    min_wacc2 = min(W_ACC2[i:i+32])
    min_wacc3 = min(W_ACC3[i:i+32])
    mn_wacc1.append(min_wacc1)
    mn_wacc2.append(min_wacc2)
    mn_wacc3.append(min_wacc3)

    #Extracting maximum values and appending to a list
    max_wacc1 = max(W_ACC1[i:i+32])
    max_wacc2 = max(W_ACC2[i:i+32])
    max_wacc3 = max(W_ACC3[i:i+32])
    mx_wacc1.append(max_wacc1)
    mx_wacc2.append(max_wacc2)
    mx_wacc3.append(max_wacc3)


for i in range(0, len(W_BVP),64) :

    mean_wbvp = mean(W_BVP[i:i+64])
    avg_wbvp.append(mean_wbvp)

    std_wbvp = stdev(W_BVP[i:i+64])
    s_wbvp.append(std_wbvp)

    min_wbvp = min(W_BVP[i:i+64])
    mn_wbvp.append(min_wbvp)

    max_wbvp = max(W_BVP[i:i+64])
    mx_wbvp.append(max_wbvp)


for i in range(0, len(W_EDA),4) :

    mean_weda = mean(W_EDA[i:i+4])
    avg_weda.append(mean_weda)

    std_weda = stdev(W_EDA[i:i+4])
    s_weda.append(std_weda)

    min_weda = min(W_EDA[i:i+4])
    mn_weda.append(min_weda)

    max_weda = max(W_EDA[i:i+4])
    mx_weda.append(max_weda)


for i in range(0, len(W_TEMP),4) :

    mean_wtemp = mean(W_TEMP[i:i+4])
    avg_wtemp.append(mean_wtemp)

    std_wtemp = stdev(W_TEMP[i:i+4])
    s_wtemp.append(std_wtemp)

    min_wtemp = min(W_TEMP[i:i+4])
    mn_wtemp.append(min_wtemp)

    max_wtemp = max(W_TEMP[i:i+4])
    mx_wtemp.append(max_wtemp)


df = df.assign(Mean_Chest_ACC1 = avg_acc1)
df = df.assign(Mean_Chest_ACC2 = avg_acc2)
df = df.assign(Mean_Chest_ACC3 = avg_acc3)
df = df.assign(Mean_Chest_EDA = avg_eda)
df = df.assign(Mean_Chest_EMG = avg_emg)
df = df.assign(Mean_Chest_Temp = avg_temp)
df = df.assign(Mean_Chest_Resp = avg_resp)
df = df.assign(Mean_Chest_ECG = avg_ecg)
df = df.assign(Mean_Wrist_ACC1 = avg_wacc1)
df = df.assign(Mean_Wrist_ACC2 = avg_wacc2)
df = df.assign(Mean_Wrist_ACC3 = avg_wacc3)
df = df.assign(Mean_Wrist_BVP = avg_wbvp)
df = df.assign(Mean_Wrist_EDA = avg_weda)
df = df.assign(Mean_Wrist_TEMP = avg_wtemp)


df = df.assign(SD_Chest_ACC1 = s_acc1)
df = df.assign(SD_Chest_ACC2 = s_acc2)
df = df.assign(SD_Chest_ACC3 = s_acc3)
df = df.assign(SD_Chest_EDA = s_eda)
df = df.assign(SD_Chest_EMG = s_emg)
df = df.assign(SD_Chest_Temp = s_temp)
df = df.assign(SD_Chest_Resp = s_resp)
df = df.assign(SD_Chest_ECG = s_ecg)
df = df.assign(SD_Wrist_ACC1 = s_wacc1)
df = df.assign(SD_Wrist_ACC2 = s_wacc2)
df = df.assign(SD_Wrist_ACC3 = s_wacc3)
df = df.assign(SD_Wrist_BVP = s_wbvp)
df = df.assign(SD_Wrist_EDA = s_weda)
df = df.assign(SD_Wrist_TEMP = s_wtemp)


df = df.assign(Min_Chest_ACC1 = mn_acc1)
df = df.assign(Min_Chest_ACC2 = mn_acc2)
df = df.assign(Min_Chest_ACC3 = mn_acc3)
df = df.assign(Min_Chest_EDA = mn_eda)
df = df.assign(Min_Chest_EMG = mn_emg)
df = df.assign(Min_Chest_Temp = mn_temp)
df = df.assign(Min_Chest_Resp = mn_resp)
df = df.assign(Min_Chest_ECG = mn_ecg)
df = df.assign(Min_Wrist_ACC1 = mn_wacc1)
df = df.assign(Min_Wrist_ACC2 = mn_wacc2)
df = df.assign(Min_Wrist_ACC3 = mn_wacc3)
df = df.assign(Min_Wrist_BVP = mn_wbvp)
df = df.assign(Min_Wrist_EDA = mn_weda)
df = df.assign(Min_Wrist_TEMP = mn_wtemp)



df = df.assign(Max_Chest_ACC1 = mx_acc1)
df = df.assign(Max_Chest_ACC2 = mx_acc2)
df = df.assign(Max_Chest_ACC3 = mx_acc3)
df = df.assign(Max_Chest_EDA = mx_eda)
df = df.assign(Max_Chest_EMG = mx_emg)
df = df.assign(Max_Chest_Temp = mx_temp)
df = df.assign(Max_Chest_Resp = mx_resp)
df = df.assign(Max_Chest_ECG = mx_ecg)
df = df.assign(Max_Wrist_ACC1 = mx_wacc1)
df = df.assign(Max_Wrist_ACC2 = mx_wacc2)
df = df.assign(Max_Wrist_ACC3 = mx_wacc3)
df = df.assign(Max_Wrist_BVP = mx_wbvp)
df = df.assign(Max_Wrist_EDA = mx_weda)
df = df.assign(Max_Wrist_TEMP = mx_wtemp)


#df = df.assign(Wrist_EDA = W_EDA)
#df = df.assign(Wrist_Temp = W_TEMP)

df = df.assign(Label = l)

df = df[(df.Label != 5) & (df.Label != 6) & (df.Label != 7)]

df.to_csv(r'#Enter Path name', index = False)
