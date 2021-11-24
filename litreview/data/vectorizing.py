<<<<<<< HEAD
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
=======
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
>>>>>>> 8fa3e8ffef9446402bd83eba11bb922602d1052d

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
<<<<<<< HEAD
import gensim
from gensim.models import Word2Vec

def vector_w2v(df, vector_size=1):
    lst_clean_abstracts = list(df["clean_abstract"])
    model = Word2Vec(sentences=lst_clean_abstracts, vector_size=vector_size)

    for index, row in df.iterrows():
        print(row["clean_abstract"])
        lst = [model.wv[word] for word in row["clean_abstract"]]
        print(lst)
        #df["vectorized_w2v"][index] = lst

    #print(df["vectorized_wsv"][0])
=======
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
>>>>>>> 8fa3e8ffef9446402bd83eba11bb922602d1052d

# LDA? or some other model?
    #return model.wv.vectors


    # df["vectorized_vaules"] = [value for value in word2vec.wv[]]
