#Average time that incidents spend with a particular Support group (Assigned_Group).

import pandas as pd

INCIDENTS =pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENTS.csv', low_memory= False)

INCIDENT_OWNER_HISTORY = pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENT_OWNER_HISTORY.csv', low_memory= False)

INCIDENT_HISTORY = pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENT_HISTORY.csv', low_memory = False)

q3 = INCIDENT_OWNER_HISTORY.groupby('assigned_group').mean().reset_index()
print(q3.sort_values(by='TIME_IN_STATUS_BY_OWNER_HRS', ascending= False))

'''
        assigned_group                  MTRS
373       ITS00386                  2128.316667
554       SM000541                  1973.583333
221       EDC00080                  1771.750000
476       NW000468                  1766.233333
403       NSD00012                  1639.316667
'''