# Is there a correlation between the number of times an incident is reassigned and
# how long it takes to restore?

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

INCIDENTS =pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENTS.csv', low_memory= False)

INCIDENT_OWNER_HISTORY = pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENT_OWNER_HISTORY.csv', low_memory= False)

INCIDENT_HISTORY = pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENT_HISTORY.csv', low_memory = False)

list=['ticket_nmbr','assigned_group']
data=INCIDENT_OWNER_HISTORY[list]
d=data.dropna(axis=0)
print(d.isnull().sum())
ticket=np.array(d['ticket_nmbr'])
assign=np.array(d['assigned_group'])
m=[]
for i in range(len(ticket)-1):
    j=i+1
    if ticket[i] == ticket[j] and assign[i] != assign[j]:
        m.append(ticket[i])
dict = {}
for key in m:
    dict[key] = dict.get(key, 0) + 1

df=pd.DataFrame(dict,index=[0])
df1=df.T.rename(columns={0:'NoT'})
df2=df1.reset_index()
df3=df2.rename(columns={'index':'ticket_nmbr'})


df4=INCIDENT_HISTORY[['ticket_nmbr','TIME_IN_STATUS_HRS']]
df4=df4.groupby('ticket_nmbr').sum()
df4=df4.reset_index()


merge=pd.merge(df4, df3, how='left', on='ticket_nmbr')
#merge.fillna(0,inplace=True)
table=merge.dropna()
print(table)



'''
       ticket_nmbr  TIME_IN_STATUS_HRS  NoT
6       IN10028618          110.433333  3.0
10      IN10028628            0.550000  1.0
11      IN10028629          152.100000  1.0
25      IN10028648            3.166667  1.0
27      IN10028651            3.450000  1.0
...            ...                 ...  ...
225985  IN10293178            0.000000  1.0
225994  IN10293190            0.000000  1.0
225995  IN10293191            0.000000  1.0
225996  IN10293193            0.000000  1.0
226003  IN10293205            0.000000  1.0
'''