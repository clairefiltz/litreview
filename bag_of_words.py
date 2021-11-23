

from sklearn.feature_extraction.text import CountVectorizer

def vectorize(df):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df.clean_abstract_text)
    X_vectorized = X.toarray()
    X_vectorized.sum()

    vectorize(df)
