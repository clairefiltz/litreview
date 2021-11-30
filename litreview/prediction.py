from litreview.params import BUCKET_NAME
import joblib
from google.cloud import storage
import os
import time

def predictor(text, neighbors):
    # download model from GCP
    #start_time = time.time()
    #print('=> ',start_time)
    #client = storage.Client().bucket(BUCKET_NAME)
    #print('aqui')
    #storage_location = 'models/knn500k.joblib'
    #blob = client.blob(storage_location)
    #blob.download_to_filename('knn500k.joblib')
    #print('=> model downloaded from GCP ', time.time()-start_time)


    start_ti = time.time()
    imported_vec = joblib.load('vec500k.joblib')
    print('=> vectorizer imported from Docker', time.time() - start_ti)

    start_time = time.time()
    imported_knn = joblib.load('knn500k.joblib')
    print('=> model imported from Docker ', time.time() - start_time)
    #imported_knn = joblib.load('https://storage.googleapis.com/wagon-data-735-vianadeabreu/models/knn500k.joblib')
    #rm = True
    #if rm:
    #    os.remove('knn500k.joblib')

    # download vectorizer
    #start_time = time.time()
    #client = storage.Client().bucket(BUCKET_NAME)
    #storage_location = 'models/vec500k.joblib'
    #blob = client.blob(storage_location)
    #blob.download_to_filename('vec500k.joblib')
    #print('=> vectorizer downloaded from GCP', time.time() - start_time)
    #start_ti = time.time()
    #imported_vec = joblib.load('vec500k.joblib')
    #print('=> vectorizer imported from Docker', time.time() - start_ti)
    #imported_vec = joblib.load('https://storage.googleapis.com/wagon-data-735-vianadeabreu/models/vec500k.joblib')
    #rm = True
    #if rm:
    #   os.remove('vec500k.joblib')

    # transform input into vectorizer
    start_time = time.time()
    vectorized_user_input = imported_vec.transform([text])
    print('=> input user transformed', time.time() - start_time)

    ## predict the kneighbours with the knn model. return the indices
    start_time = time.time()
    indices = imported_knn.kneighbors(vectorized_user_input,neighbors,return_distance=False)
    print('=> prediction done', time.time() - start_time)
    print('=> indices',indices)
    result = {'indices': [int(i) for i in indices[0]]}
    return result
