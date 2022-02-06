# Number of times an incident is reassigned during the life of the ticket.

import pandas as pd
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

print(df3)