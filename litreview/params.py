## path for the local data base
LOCAL_CSV = 'test'

## from GCP ##
BUCKET_NAME = 'wagon-data-735-vianadeabreu'
PROJECT_ID ='le-wagon-data-735-vianadeabreu'
LOCATION = 'EU'


def check_table_name(x):
    tables = list(range(99999, 1978108, 100000))
    tables.append(1978108)
    for i in range(len(tables)+1):
        #print(tables[i])
        if x <= tables[i]:
            return str(tables[i])
    return None


#print('aqui', check_table_name(346732))
