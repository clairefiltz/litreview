from gensim.models import Word2Vec
import numpy as np
import pandas as pd
import os
from litreview.data import preprocessing


dirname = os.path.dirname(__file__)
path_model = os.path.join(dirname, '../../raw_data/model')
path_csv = os.path.join(dirname, '../../raw_data/trimmed_arxiv_docs5000.csv')
word2vec_filename = os.path.join(dirname, '../../raw_data/w2c.csv')
# load the model which is saved in the raw_data/model
# then read the csv
model = Word2Vec.load(path_model)
df = preprocessing.preprocessing(path_csv)

print(np.mean([model.wv[token] for token in df['clean_abstract'][0]], axis=0))



with open(word2vec_filename, 'w+') as word2vec_file:
    for index, row in df.iterrows():
        model_vector = (np.mean(
            [model.wv[token] for token in row['clean_abstract']],
            axis=0)).tolist()
        if index == 0:
            header = ",".join(str(ele) for ele in range(10))
            word2vec_file.write(header)
            word2vec_file.write("\n")
        # Check if the line exists else it is vector of zeros
        if type(model_vector) is list:
            line1 = ",".join(
                [str(vector_element) for vector_element in model_vector])
        else:
            line1 = ",".join([str(0) for i in range(10)])
        word2vec_file.write(line1)
        word2vec_file.write('\n')







#### old version

'''# instatiate the model
    lst_clean_abstracts = list(df["clean_abstract"])
    vectorizer = Word2Vec(sentences=lst_clean_abstracts, vector_size=vector_size, min_count=1)
    def vec_mean(x):
        return [vectorizer.wv[word] for word in x]
    new_df['vectorized_w2v'] = new_df["clean_abstract"].apply(lambda x:vec_mean(x))
    new_df['mean_vectorized_w2v'] = new_df['vectorized_w2v'].apply(lambda x:np.mean(x,axis=0))

    tmp2 = [x['mean_vectorized_w2v'].tolist() for _, x in new_df.iterrows()]
    return np.array([tmp2],dtype='float64')'''
