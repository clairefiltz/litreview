from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from litreview import preprocessing, prediction


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

    return prediction.predictor(text,neighbors)
