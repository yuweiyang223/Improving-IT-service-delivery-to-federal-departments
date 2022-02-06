# Is there correlation between the number of tickets
# associated with a particular assigned group,
# organization or service and the time it takes to restore
# service?

import pandas as pd


INCIDENTS =pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENTS.csv', low_memory= False)

INCIDENT_OWNER_HISTORY = pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENT_OWNER_HISTORY.csv', low_memory= False)

INCIDENT_HISTORY = pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENT_HISTORY.csv', low_memory = False)

reasonable_inc = INCIDENTS[INCIDENTS.OPEN_DATE <= INCIDENTS.CLOSE_DATE]

def f(x):
    data = reasonable_inc[['TICKET_NMBR', x]]
    data1=pd.DataFrame(INCIDENT_OWNER_HISTORY.groupby('ticket_nmbr')['TIME_IN_STATUS_BY_OWNER_HRS'].sum())
    data2 = data.rename(columns={'TICKET_NMBR': 'ticket_nmbr'})
    data_use = pd.merge(data1, data2, on = 'ticket_nmbr')
    NoT_org = pd.DataFrame(data_use.groupby(x)['ticket_nmbr'].count().reset_index())
    ToU_org = pd.DataFrame(data_use.groupby(x)['TIME_IN_STATUS_BY_OWNER_HRS'].mean().reset_index())
    corr_NTU = pd.merge(NoT_org, ToU_org, on = x)
    return corr_NTU.sort_values(by = 'TIME_IN_STATUS_BY_OWNER_HRS', ascending= False)

# print(f('org_id'))

'''
    index  org_id  ticket_nmbr  TIME_IN_STATUS_BY_OWNER_HRS
37     37  1083.0            6                  1923.686111
6       6   918.0            2                  1061.750000
16     16  1030.0            9                   589.961111
38     38  1085.0            4                   551.216667
42     42  1182.0            6                   514.800000
..    ...     ...          ...                          ...
1       1   837.0            1                     1.366667
12     12   988.0            2                     0.033333
7       7   930.0            2                     0.000000
9       9   948.0            1                     0.000000
48     48  1232.0            1                     0.000000

'''
# print(f('service'))

'''
                                      service  ...  TIME_IN_STATUS_BY_OWNER_HRS
32                      IT Continuity Support Service  ...                 15832.500000
54                                          Satellite  ...                  1134.643056
35                    Intra-building Network Services  ...                   952.217096
46                                     Mobile Devices  ...                   567.069697
47      Other - Account & Service Delivery Management  ...                   564.641667
..                                                ...  ...                          ...
56  Service Management - Enterprise Control Center...  ...                    16.550000
0                                                  -1  ...                     5.402045
1                                          Bulk Print  ...                     1.990000
34                                           Internet  ...                     0.000000
14                     Faciltiies-as-a-service (FaaS)  ...                     0.000000

[63 rows x 3 columns]
'''

print(f('ASSIGNED_GROUP'))

'''
    ASSIGNED_GROUP  ticket_nmbr  TIME_IN_STATUS_BY_OWNER_HRS
215       ITS00302            1                 19883.066667
45        DC000143            1                 16757.966667
405       SM000541            1                 15832.500000
325       NW000435            1                 13199.600000
96        DC000218            1                 10930.216667
..             ...          ...                          ...
140       EDC00028            1                     0.000000
402       SM000521            1                     0.000000
382       NW000511            1                     0.000000
373       NW000498            1                     0.000000
122       DC000269            2                     0.000000
'''