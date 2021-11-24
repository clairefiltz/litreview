from sklearn.neighbors import NearestNeighbors

def KNN(df, n_neighbors):
    model = NearestNeighbors(n_neighbors=n_neighbors, algorithm='brute')
    model.fit(df)
    return model
