from google.cloud import storage
import joblib
from litreview import preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import os
### GCP configuration - - - - - - - - - - - - - - - - - - -

# /!\ you should fill these according to your account

### GCP Project - - - - - - - - - - - - - - - - - - - - - -

# not required here

### GCP Storage - - - - - - - - - - - - - - - - - - - - - -

BUCKET_NAME = 'wagon-data-735-vianadeabreu'

##### Data  - - - - - - - - - - - - - - - - - - - - - - - -

# train data file location
# /!\ here you need to decide if you are going to train using the provided and uploaded data/train_1k.csv sample file
# or if you want to use the full dataset (you need need to upload it first of course)
BUCKET_TRAIN_DATA_PATH = 'data/trimmed_arxiv_docs5000csv'
#gs://wagon-data-735-vianadeabreu/data/trimmed_arxiv_docs.csv
##### Training  - - - - - - - - - - - - - - - - - - - - - -

# not required here

##### Model - - - - - - - - - - - - - - - - - - - - - - - -

# model folder name (will contain the folders for all trained model versions)
MODEL_NAME = 'knn_model'

# model version folder name (where the trained model.joblib file will be stored)
MODEL_VERSION = 'v1'
#local_model_name = 'model.joblib'
#local_vec_name = 'vec.joblib'
### GCP AI Platform - - - - - - - - - - - - - - - - - - - -

# not required here

### - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def get_data():
    """method to get the training data (or a portion of it) from google cloud bucket"""
    #df = preprocessing.preprocessing(
    #f"gs://{BUCKET_NAME}/{BUCKET_TRAIN_DATA_PATH}")  #, nrows=1000)
    print("read data from bucket")
    df = preprocessing.preprocessing(
        "gs://wagon-data-735-vianadeabreu/data/arxiv-metadata_final.csv")  #, nrows=1000)
    #gs://wagon-data-735-vianadeabreu/data/trimmed_arxiv_docs5000.csv
    return df

def train_model(df, i):
    # should get the data frame and return a model.fit
    # instantiate and fit the model
    vec = TfidfVectorizer(max_features=i).fit(df['clean_abstract_text'])
    print("=> vec fitted")
    X_vectorized = vec.transform(df['clean_abstract_text'])
    print("=> vec transformed")
    knn = NearestNeighbors(n_neighbors=10).fit(X_vectorized)
    print("=> knn fitted")
    return knn, vec

def save_model_to_gcp(model, vec, model_version, model_name, vec_name,rm=True):
    """Save the model into a .joblib and upload it on Google Storage /models folder
    HINTS : use sklearn.joblib (or jbolib) libraries and google-cloud-storage"""
    #local_model_name = 'model.joblib'
    # saving the trained model to disk (which does not really make sense
    # if we are running this code on GCP, because then this file cannot be accessed once the code finished its execution)
    local_model_name = f"{model_name}_final_v{model_version}.joblib"
    local_vec_name = f"{vec_name}_final_v{model_version}.joblib"
    joblib.dump(model, local_model_name)
    print("saved model.joblib locally")
    client = storage.Client().bucket(BUCKET_NAME)
    storage_location = f"models/{local_model_name}"
    blob = client.blob(storage_location)
    blob.upload_from_filename(local_model_name)
    print(
        "uploaded model.joblib to gcp cloud storage under \n => {}".format(
            storage_location))
    if rm:
        os.remove(local_model_name)

    ##### same for vec
    joblib.dump(vec, local_vec_name)
    print("saved vec.joblib locally")
    client = storage.Client().bucket(BUCKET_NAME)
    storage_location = f"models/{local_vec_name}"
    blob = client.blob(storage_location)
    blob.upload_from_filename(local_vec_name)
    print("uploaded model.joblib to gcp cloud storage under \n => {}".format(
        storage_location))
    if rm:
        os.remove(local_vec_name)


if __name__ == '__main__':
    # get training data from GCP bucket
    df = get_data()

    # train model (locally if this file was called through the run_locally command
    # or on GCP if it was called through the gcp_submit_training, in which case
    # this package is uploaded to GCP before being executed)
    knn, vec = train_model(df,100)
    # save trained model to GCP bucket (whether the training occured locally or on GCP)
    save_model_to_gcp(knn, vec, 100,'knn_final','vec5k')
