# imports
from sklearn.feature_extraction.text import CountVectorizer
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import os


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

def tfidf(df):

    texts = df['clean_abstract_text']
    vectorizer = TfidfVectorizer()
    X_new = vectorizer.fit_transform(texts)
    X_tfidf =X_new.toarray()
    X_vectorized = pd.DataFrame(X_tfidf, columns=vectorizer.get_feature_names_out())
    return X_vectorized

# Word2Vec
# get one preprocessed data frame as input and return a data frame vectorized
def vector_w2v(df, vector_size=100):
    #copy to be safe with the data
    df_copy = df.copy()
    model = Word2Vec(df_copy.clean_abstract.values.tolist(),
                     vector_size=vector_size,
                     min_count=1)
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../raw_data/w2c.csv')
    with open(filename, 'w+') as word2vec_file:
        for index, row in df_copy.iterrows():
            model_vector = (np.mean([model.wv[word] for word in row['clean_abstract']],axis=0)).tolist()
            if index == 0:
                header = ",".join(str(ele) for ele in range(vector_size))
                word2vec_file.write(header)
                word2vec_file.write("\n")
            # Check if the line exists else it is vector of zeros
            if type(model_vector) is list:
                line1 = ",".join([str(vector_element) for vector_element in model_vector])
            else:
                line1 = ",".join([str(0) for i in range(vector_size)])
            word2vec_file.write(line1)
            word2vec_file.write('\n')

    vectorized_df = pd.DataFrame(pd.read_csv(filename))
    return vectorized_df

# LDA? or some other model?
#return model.wv.vectors


# df["vectorized_vaules"] = [value for value in word2vec.wv[]]


def vector_w2v_new(df, vector_size=100):
    #copy to be safe with the data
    df_copy = df.copy()
    model = Word2Vec(df_copy.clean_abstract.values.tolist(),
                     vector_size=vector_size,
                     min_count=1)
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../raw_data/w2complete.csv')
    with open(filename, 'w+') as word2vec_file:
        list_words = model.wv.index_to_key
        for index, row in df_copy.iterrows():
            if index == 0:
                header = ",".join(str(word) for word in list_words)
                word2vec_file.write(header)
                word2vec_file.write("\n")
            abstract_vector = []
            for word in list_words:
                if word in row['clean_abstract']:
                    abstract_vector.append(np.mean(model.wv[word]))
                else:
                    abstract_vector.append(0.0)
            line = ",".join([str(vector_element) for vector_element in abstract_vector])
            word2vec_file.write(line)
            word2vec_file.write('\n')

    vectorized_df = pd.DataFrame(pd.read_csv(filename))
    return vectorized_df
