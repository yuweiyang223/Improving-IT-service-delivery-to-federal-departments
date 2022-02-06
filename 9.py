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




df4=INCIDENT_HISTORY[['ticket_nmbr','TIME_IN_STATUS_HRS']]
df4=df4.groupby('ticket_nmbr').sum()
df4=df4.reset_index()

EXTERNAL_SYSTEM = INCIDENTS[['TICKET_NMBR','EXTERNAL_SYSTEM']].rename(columns ={'TICKET_NMBR':'ticket_nmbr' })
reassign = df3
E_and_re = pd.merge(EXTERNAL_SYSTEM, reassign, how='left', on='ticket_nmbr')
E_and_re_sort = E_and_re.groupby('EXTERNAL_SYSTEM').count().sort_values(by='ticket_nmbr',ascending=False)
E_and_re_sort = E_and_re_sort.reset_index()
E_and_re_not = E_and_re.groupby('EXTERNAL_SYSTEM').mean().sort_values(by='NoT',ascending=False).reset_index()
merge = pd.merge(E_and_re_not,E_and_re_sort,how='left', on='EXTERNAL_SYSTEM')
time = pd.merge(df4,EXTERNAL_SYSTEM,how='left', on='ticket_nmbr')
EXTERNAL_SYSTEM_merge = pd.merge(time,E_and_re,how='left', on='ticket_nmbr')
EXTERNAL_SYSTEM_merge.drop(['EXTERNAL_SYSTEM_y'],inplace=True,axis=1)
table = EXTERNAL_SYSTEM_merge.groupby('EXTERNAL_SYSTEM_x').mean().reset_index().sort_values(by='TIME_IN_STATUS_HRS',ascending=False)
colNameDict = {'EXTERNAL_SYSTEM_x':'EXTERNAL_SYSTEM'}
table.rename(columns = colNameDict,inplace=True)
table1 = pd.merge(merge, table, how='left', on='EXTERNAL_SYSTEM').sort_values(by='TIME_IN_STATUS_HRS',ascending=False)
table2=table1[table1.ticket_nmbr>=100]
print(table2)

'''
        EXTERNAL_SYSTEM     NoT_x  ...  TIME_IN_STATUS_HRS       NoT
11          SELFSERVICE  1.500000  ...          122.359845  1.500000
8   EXTERNALSERVICEDESK  1.775120  ...          120.986885  1.769231
5   CREATEDFROMINCIDENT  1.853659  ...          116.744837  1.853659
3         CREATEDFROMSR  1.895383  ...          102.291396  1.895511
7                 EMAIL  1.783534  ...           99.152460  1.782407
9             PHONECALL  1.728216  ...           50.323066  1.723205
12      EVENTMANAGEMENT  1.263818  ...           28.753661  1.263962

'''