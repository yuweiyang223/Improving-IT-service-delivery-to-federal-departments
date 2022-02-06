# Is there a correlation between assigned groups and the length of time tickets spend in certain status?

import pandas as pd

INCIDENTS =pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENTS.csv', low_memory= False)

INCIDENT_OWNER_HISTORY = pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENT_OWNER_HISTORY.csv', low_memory= False)

INCIDENT_HISTORY = pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENT_HISTORY.csv', low_memory = False)

incident_owner2 = INCIDENT_OWNER_HISTORY[['ticket_nmbr', 'STATUS', 'assigned_group', 'TIME_IN_STATUS_BY_OWNER_HRS']]

q7 = incident_owner2.groupby(['STATUS', 'assigned_group']).agg({'TIME_IN_STATUS_BY_OWNER_HRS':'sum'}).reset_index()
q7a = q7[q7.TIME_IN_STATUS_BY_OWNER_HRS != 0]
print(q7a.sort_values(by = 'TIME_IN_STATUS_BY_OWNER_HRS', ascending=False))

'''
          STATUS assigned_group  TIME_IN_STATUS_BY_OWNER_HRS
2511      QUEUED       ESI00011                 1.526503e+06
591     AWAITVEN       DC000132                 1.033334e+06
2675      QUEUED       NW000417                 6.333149e+05
2661      QUEUED       NW000403                 6.148947e+05
2670      QUEUED       NW000412                 6.032582e+05
...          ...            ...                          ...
1815     PENDING       ENT00005                 1.666667e-02
37      AWAITCHG       DC000147                 1.666667e-02
1564      INPROG       ITS00337                 1.666667e-02
3395     SLAHOLD       EDC00051                 1.666667e-02
2061  PENDINGREV       DC000125                 1.666667e-02
'''