from litreview.data import preprocessing
from urllib.request import urlopen
import joblib
import pandas as pd


#DATABASE = 'https://storage.googleapis.com/wagon-data-735-vianadeabreu/data/trimmed_arxiv_docs.csv'
#PATH_MODEL = 'kmeans_10_000_rows_30_clusters.joblib'
#PATH_MODEL = 'knn500k.joblib'
#PATH_VEC = 'vec500k.joblib'

DATABASE = 'https://storage.googleapis.com/wagon-data-735-vianadeabreu/data/trimmed_arxiv_docs.csv'
#PATH_MODEL = 'https://storage.googleapis.com/wagon-data-735-vianadeabreu/models/kmeans_10_000_rows_30_clusters.joblib'
PATH_MODEL = 'https://storage.googleapis.com/wagon-data-735-vianadeabreu/models/knn500k.joblib'
PATH_VEC = 'https://storage.googleapis.com/wagon-data-735-vianadeabreu/models/vec500k.joblib'


def run_main(user_input, neighbors=3):
    user_input = preprocessing.input_preprocessing(user_input)

    ## this is for running the search with kmeans model
    # model = joblib.load(PATH_MODEL)
    # result = model.predict([user_input])

    ## this is for running the search with knn model
    # import the model and the vecorizer from a joblib
    imported_knn = joblib.load(urlopen(PATH_MODEL))
    imported_vec = joblib.load(urlopen(PATH_VEC))

    ## transform user input to vectorizer
    vectorized_user_input = imported_vec.transform([user_input])

    ## predict the kneighbours with the knn model. return the indices
    indices = imported_knn.kneighbors(vectorized_user_input,
                            neighbors,
                            return_distance=False)

    result = []
    df = pd.read_csv(DATABASE)
    for j in range(1,len(indices[0])):
        tmp = df.loc[indices[0][j], ['title', 'authors', 'abstract']].tolist()
        result.append(tmp)
    return result


#print(run_main('math, history, medicine, look for the life'))
