# Mean time to restore service (MTRS), are there particular services that
# are taking longer on average to be restored?

import pandas as pd
import numpy as np

INCIDENTS =pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENTS.csv', low_memory= False)

INCIDENT_OWNER_HISTORY = pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENT_OWNER_HISTORY.csv', low_memory= False)

INCIDENT_HISTORY = pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENT_HISTORY.csv', low_memory = False)


inprocess_owner1 = INCIDENT_OWNER_HISTORY[INCIDENT_OWNER_HISTORY.STATUS != 'CLOSED']
q4 = inprocess_owner1.groupby('service')['TIME_IN_STATUS_BY_OWNER_HRS'].mean().reset_index()
print(q4.sort_values(by = 'TIME_IN_STATUS_BY_OWNER_HRS', ascending= False))

'''
                                service                       MTRS
33        IT Continuity Support Service                  1973.583333
63                     WTD Provisioning                   625.816667
57  Solutions Integration Service (SIS)                   428.064286
0                            Bulk Print                   377.007738
28                        IBN - Cabling                   346.957143
..                                  ...                          ...
38         Managed Secure File Transfer                    13.037097
45                Mobile - Voice & Data                    12.936081
36                            Mainframe                    12.075492
16                      Fixed - Centrex                     9.989080
25    HPC - Interaction & Visualization                     9.812861
'''