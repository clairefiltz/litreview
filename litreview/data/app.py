import preprocessing
import vectorizing
import trainer
import pandas as pd

def run_app(path_df, vectorizer, model, n_neighbors=0, abstract=None):
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
            print(indices)
        return "Everything done!"

print(run_app("/home/felix/code/clairefiltz/litreview/raw_data/subset_100.csv", "word2vec", "KNN", 3))
