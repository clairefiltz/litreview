from litreview.data import preprocessing, vectorizing, trainer
import pandas as pd
import os
from api import fast


PATH = 'gs://litreview-bucket/litreview-bucket/trimmed_arxiv_docs5000.csv'
VECTORIZER = 'tfidf'
MODEL = 'KNN'
N_NEIB = 3
def run_search(path_df=PATH, vectorizer=VECTORIZER, model=MODEL, n_neighbors=N_NEIB, abstract=None):
    df = preprocessing.preprocessing(path_df)
    if vectorizer == "bag_of_words":
        X_vectorized = vectorizing.bag_of_words(df)
    elif vectorizer == "tfidf":
        X_vectorized = vectorizing.tfidf(df)
    elif vectorizer =="word2vec":
        X_vectorized = vectorizing.vector_w2v(df)
    else:
        return "ERROR - vectorizer does not exist"

    if model == "KNN":
        model = trainer.KNN(X_vectorized, n_neighbors)
        distances, indices = model.kneighbors(X_vectorized)
        if abstract != None:
           print(indices[abstract])
        else:
            result = {}
            for i in range(len(indices)):
                tmp = []
                for j in range(1,n_neighbors):
                    tmp.append(df.loc[indices[i][j],'title'])
                result[df.loc[indices[i][0],'title']] = tmp
            return result

#print(run_search()['Triangulated categories of relative 1-motives'])
