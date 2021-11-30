from litreview import preprocessing
import joblib
import pandas as pd
from google.cloud import storage

PATH_MODEL = 'gs://wagon-data-735-vianadeabreu/models/knn500k.joblib'
PATH_VEC = 'gs://wagon-data-735-vianadeabreu/models/vec500k.joblib'
DATABASE = 'gs://wagon-data-735-vianadeabreu/data/trimmed_arxiv_docs.csv'
BUCKET_NAME = 'wagon-data-735-vianadeabreu'



def run_main(path_data):
    # this function should load the data set, preprocessing,
    # train the model locally or on gcp and save it locally or gcp
    return None
if __name__ == '__main__':
    run_main()


#print(run_main('math, history, medicine, look for the life'))
