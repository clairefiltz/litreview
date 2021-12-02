from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from litreview import preprocessing, prediction, params
import time
from google.cloud import bigquery

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return {"greeting": "Hello world"}

@app.get("/predict")
def predict(user_input, neighbors=3):
    # neighbors have to be int
    neighbors = int(neighbors)
    # preprocessing the input from the user
    text = preprocessing.input_preprocessing(user_input)
    print('=> input preprocessed')

    indices = prediction.predictor(text, neighbors)['indices']

    result = {}
    pos_neigh = 0
    start_time = time.time()
    client = bigquery.Client(project=params.PROJECT_ID,
                             location=params.LOCATION)
    for i in indices:
        table500k = params.check_table_name(i)
        #data_set = 'arxiv500'
        data_set = 'arxiv'
        query = f"""SELECT index,id,title,abs
		        FROM {params.PROJECT_ID}.{data_set}.{table500k} WHERE index={i}"""
        query_job = client.query(query)
        data = query_job.to_dataframe()
        title = data.loc[0,'title']
        abstract = data.loc[0,'abs']
        id = data.loc[0, 'id']
        result[pos_neigh] = [title, abstract, id]
        pos_neigh += 1
    end_time = time.time()
    print('=> query done ', end_time - start_time)
    print(type(result))

    return result
