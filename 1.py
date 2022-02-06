
# Average time that incidents spend in a particular status.


import pandas as pd

INCIDENT_HISTORY = pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENT_HISTORY.csv', low_memory = False)
# result = INCIDENT_HISTORY.groupby(by='STATUS').mean().reset_index()
#print(result.sort_values(by='TIME_IN_STATUS_HRS',ascending= False))

'''
      STATUS        TIME_IN_STATUS_HRS
10  PENDINGREV          223.411555
2     AWAITVEN          137.735532
8   PENDINGCHG          125.241167
0     AWAITCHG          113.363088
14     SLAHOLD          108.268436
11  PENDINGVEN          102.578170
9   PENDINGCUS           79.481625
1     AWAITCUS           69.843384
7      PENDING           65.869582
5       INPROG           26.993950
12      QUEUED           24.715884
4     HISTEDIT           23.380726
6          NEW            0.324458
13    RESOLVED            0.146312
3       CLOSED                 NaN
'''




result1 = INCIDENT_HISTORY.groupby(by='STATUS').count().reset_index()
print(result1[['STATUS', 'ticket_nmbr']])

'''
        STATUS  count
0     AWAITCHG         3642
1     AWAITCUS        28788
2     AWAITVEN        15983
3       CLOSED       223238
4     HISTEDIT          183
5       INPROG       104608
6          NEW       155661
7      PENDING         1315
8   PENDINGCHG          100
9   PENDINGCUS         1112
10  PENDINGREV          626
11  PENDINGVEN          723
12      QUEUED       312310
13    RESOLVED       224254
14     SLAHOLD        11454
'''