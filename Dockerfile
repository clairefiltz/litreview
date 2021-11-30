FROM python:3.8.6-buster

COPY api /api
COPY litreview /litreview
COPY models_knn500k.joblib /knn500k.joblib
COPY models_vec500k.joblib /vec500k.joblib
COPY requirements.txt /requirements.txt
#COPY /Users/viana.abreu/Downloads/le-wagon-data-735-vianadeabreu-328483ac66e4.json /credentials.json
RUN pip install -r requirements.txt

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
