# MTRS of Assigned Groups Based On Priority

import pandas as pd

INCIDENTS =pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENTS.csv', low_memory= False)

INCIDENT_OWNER_HISTORY = pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENT_OWNER_HISTORY.csv', low_memory= False)

INCIDENT_HISTORY = pd.read_csv(r'C:\Users\Yuwei\Desktop\case\INCIDENT_HISTORY.csv', low_memory = False)

reasonable_inc = INCIDENTS[INCIDENTS.OPEN_DATE <= INCIDENTS.CLOSE_DATE]
incidents_data = reasonable_inc[['TICKET_NMBR', 'PARENT_SERVICE', 'service', 'ASSIGNED_GROUP', 'PRIORITY', 'ACTUAL_COMPLETION_HRS', 'BUSINESS_COMPLETION_HRS', 'classification', 'EXTERNAL_SYSTEM']]
inc_his_data = INCIDENT_HISTORY[['ticket_nmbr', 'STATUS', 'TIME_IN_STATUS_HRS']]
incidents_data = incidents_data.rename(columns={'TICKET_NMBR': 'ticket_nmbr'})
time_data = pd.merge(incidents_data, inc_his_data, on = 'ticket_nmbr')
time_data_lowpri = time_data[time_data.PRIORITY == 'Low']
time_data_medpri = time_data[time_data.PRIORITY == 'Medium']
time_data_hipri = time_data[time_data.PRIORITY == 'High']
assign_low = pd.DataFrame(time_data_lowpri.groupby('ASSIGNED_GROUP')['TIME_IN_STATUS_HRS'].mean().sort_values(ascending = False))
assign_med = pd.DataFrame(time_data_medpri.groupby('ASSIGNED_GROUP')['TIME_IN_STATUS_HRS'].mean().sort_values(ascending = False))
assign_hi = pd.DataFrame(time_data_hipri.groupby('ASSIGNED_GROUP')['TIME_IN_STATUS_HRS'].mean().sort_values(ascending = False))

print(assign_hi)
'''
                TIME_IN_STATUS_HRS
ASSIGNED_GROUP                    
NW000469                637.133333
EDC00003                330.504167
ITS00326                298.730159
ESI00012                202.703333
DC000245                166.283333
'''
print(assign_med)
'''
                TIME_IN_STATUS_HRS
ASSIGNED_GROUP                    
SM000541               1054.779167
ITS00302                833.379167
ITS00337                748.077778
NW000451                558.029167
DC000196                424.309524
'''
print(assign_low)
'''
                
ASSIGNED_GROUP          TIME_IN_STATUS_HRS       
NW000435               1477.055556
DC000213               1011.494444
NW000495                830.388889
DC000218                556.800000
NW000422                425.438889
'''