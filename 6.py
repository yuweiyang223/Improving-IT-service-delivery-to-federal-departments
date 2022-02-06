# Are there particular organizations for whom it takes longer on average to restore services?

import pandas as pd
import numpy as np

INCIDENTS =pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENTS.csv', low_memory= False)

INCIDENT_OWNER_HISTORY = pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENT_OWNER_HISTORY.csv', low_memory= False)

INCIDENT_HISTORY = pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENT_HISTORY.csv', low_memory = False)

inprocess_owner1 = INCIDENT_OWNER_HISTORY[INCIDENT_OWNER_HISTORY.STATUS != 'CLOSED']

incident_q6 = INCIDENTS[['TICKET_NMBR', 'org_id']]
incidents_q6 = incident_q6.rename(columns={'TICKET_NMBR': 'ticket_nmbr'})
q6_df = pd.merge(incidents_q6, inprocess_owner1, on='ticket_nmbr')
q6 = q6_df.groupby('org_id')['TIME_IN_STATUS_BY_OWNER_HRS'].mean().reset_index()
print(q6.sort_values(by = 'TIME_IN_STATUS_BY_OWNER_HRS',ascending=False))

'''
    org_id                       MTRS 
38  1083.0                   398.004023
51  1237.0                   306.748246
39  1085.0                   175.610833
17  1030.0                   129.503659
57  1273.0                   115.716361
..     ...                          ...
13   988.0                     0.016667
10   948.0                     0.000000
49  1232.0                     0.000000
8    930.0                     0.000000
54  1248.0                          NaN

'''