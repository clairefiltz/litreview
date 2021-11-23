#imports
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy

# Bag of words

def bag_of_words(df):
    new_df = df.copy()
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(new_df.clean_abstract_text)
    X_vectorized = X.toarray()
    X_vectorized = pd.DataFrame(X_vectorized, columns=vectorizer.get_feature_names_out())
    #output_df = pd.merge(new_df, X_vectorized)

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
import gensim
from gensim.models import Word2Vec

def vector_w2v(df, vector_size=1):
    lst_clean_abstracts = list(df["clean_abstract"])
    model = Word2Vec(sentences=lst_clean_abstracts, vector_size=vector_size)

    for index, row in df.iterrows():
        print(row["clean_abstract"])
        lst = [model.wv(word) for word in row["clean_abstract"]]
        print(lst)
        #df["vectorized_w2v"][index] = lst

    #print(df["vectorized_wsv"][0])

# LDA? or some other model?
    #return model.wv.vectors


    # df["vectorized_vaules"] = [value for value in word2vec.wv[]]
