# imports
from sklearn.feature_extraction.text import CountVectorizer
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np


# Bag of words
# get one data frame as input an returns o data frame vectorized
def bag_of_words(df):
    # copy to be safe with the data
    new_df = df.copy()

    # instantiate the model
    vectorizer = CountVectorizer()

    # fit and transform and then convert to a data frame
    X = vectorizer.fit_transform(new_df.clean_abstract_text)
    X_vectorized = X.toarray()
    X_vectorized = pd.DataFrame(X_vectorized, columns=vectorizer.get_feature_names_out())

    return X_vectorized

# TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer

def tfidf(df):

    texts = df['clean_abstract_text']
    vectorizer = TfidfVectorizer()
    X_new = vectorizer.fit_transform(texts)
    X_tfidf =X_new.toarray()
    X_vectorized = pd.DataFrame(X_tfidf, columns=vectorizer.get_feature_names_out())

    return X_vectorized

# Word2Vec
# get one preprocessed data frame as input and return a data frame vectorized
def vector_w2v(df, vector_size=10):
    #copy to be safe with the data
    new_df = df.copy()

    # instatiate the model
    lst_clean_abstracts = list(df["clean_abstract"])
    vectorizer = Word2Vec(sentences=lst_clean_abstracts, vector_size=vector_size, min_count=1)
    def vec_mean(x):
        return [vectorizer.wv[word] for word in x]
    new_df['vectorized_w2v'] = new_df["clean_abstract"].apply(lambda x:vec_mean(x))
    new_df['mean_vectorized_w2v'] = new_df['vectorized_w2v'].apply(lambda x:np.mean(x,axis=1))

    return np.array([x['mean_vectorized_w2v'] for _, x in new_df.iterrows()])

# LDA? or some other model?
    #return model.wv.vectors


    # df["vectorized_vaules"] = [value for value in word2vec.wv[]]
