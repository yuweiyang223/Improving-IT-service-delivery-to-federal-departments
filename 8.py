# Is there correlation between the number of tickets
# associated with a particular assigned group,
# organization or service and the time it takes to restore
# service?

import pandas as pd


INCIDENTS =pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENTS.csv', low_memory= False)

INCIDENT_OWNER_HISTORY = pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENT_OWNER_HISTORY.csv', low_memory= False)

INCIDENT_HISTORY = pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENT_HISTORY.csv', low_memory = False)

reasonable_inc = INCIDENTS[INCIDENTS.OPEN_DATE <= INCIDENTS.CLOSE_DATE]

data8 = reasonable_inc[['TICKET_NMBR', 'org_id']]
data81 = pd.DataFrame(INCIDENT_OWNER_HISTORY.groupby('ticket_nmbr')['TIME_IN_STATUS_BY_OWNER_HRS'].sum())
data82 = data8.rename(columns={'TICKET_NMBR': 'ticket_nmbr'})
data_use = pd.merge(data81, data82, on = 'ticket_nmbr')
NoT_org = pd.DataFrame(data_use.groupby('org_id')['ticket_nmbr'].count().reset_index())

ToU_org = pd.DataFrame(data_use.groupby('org_id')['TIME_IN_STATUS_BY_OWNER_HRS'].mean().reset_index())
corr_NTU = pd.merge(NoT_org, ToU_org, on = 'org_id').reset_index()
print(corr_NTU.sort_values(by = 'TIME_IN_STATUS_BY_OWNER_HRS', ascending= False))




