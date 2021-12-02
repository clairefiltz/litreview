import streamlit as st
import requests
import pandas as pd
#import random
import time
from google.cloud import bigquery
from litreview.params import PROJECT_ID, LOCATION, check_table_name

#################
## hard codes ##
#################
API_URL = 'https://literaturreview-z37yi6v7za-ew.a.run.app/predict'
API_LOCAL = 'http://127.0.0.1:8000/predict'
#FILENAME = 'https://storage.googleapis.com/wagon-data-735-vianadeabreu/data/arxiv-metadata_final.csv'
FILENAME = 'https://storage.googleapis.com/wagon-data-735-vianadeabreu/data/trimmed_arxiv_docs.csv'

st.set_page_config(
    page_title="Automated Literature Review",  # => Quick reference - Streamlit
    page_icon="📚",
    layout="wide",  # wide
    initial_sidebar_state="auto")  # collapsed

#######################
## setup for sidebar ##
#######################
sideb = st.sidebar
sideb.image("images/logo.png", use_column_width=True)
sideb.markdown(
    "<h1 style='text-align: center; color: #5D6D7E;'>Demo Day - Batch 735 - Berlin</h1>",
    unsafe_allow_html=True)
sideb.write(
    "<h1 style='text-align: center; color: #5D6D7E; font-size: 13px;'>Claire Filtz, Felix Wohlleben</h1>",
    unsafe_allow_html=True)
sideb.write(
    "<h1 style='text-align: center; color: #5D6D7E; font-size: 13px;'>Issa Al Barwani, Alex Viana</h1>",
    unsafe_allow_html=True)

#######################
## setup for main #####
#######################
st.markdown(
    "<h1 style='text-align: center; color: #5D6D7E;'>an automated literature review tool</h1>",
    unsafe_allow_html=True)
##########################
## setup for search bar ##
##########################


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">',
                unsafe_allow_html=True)


def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>',
                unsafe_allow_html=True)


local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

# icon("search")
input_user = st.text_input("", "search...")
neighbors = st.number_input(
    '',
    min_value=2,
    max_value=30,
)
button_clicked = st.button("OK")

params = {'user_input': input_user.split(), 'neighbors': neighbors}

if button_clicked:
    #api_url
    #api_local
    #st.write('time to access the api')
    start_time = time.time()
    response = requests.get(API_URL, params=params)
    prediction = response.json()
    end_time = time.time()
    #end_time - start_time
    #result = prediction['indices']
    #prediction["0"][1]
    start_time = time.time()
    #client = bigquery.Client(project=PROJECT_ID, location=LOCATION)
    st.write(
        f"<h1 style='text-align: left; color: #5D6D7E; font-size: 18px;'>Here are {neighbors} nice papers to read:</h1>",
        unsafe_allow_html=True)
    for i in range(neighbors):
        #data = prediction[i]
        #prediction[str(i)][0]
        st.write(
            f"<h1 style='text-align: left; color: #ABB2B9; font-size: 15px;'>{prediction[str(i)][0]}</h1>",
            unsafe_allow_html=True)
        st.write(
            f"<h1 style='text-align: left; color: #ABB2B9; font-size: 15px; font-style: italic;'>{prediction[str(i)][1]}</h1>",
            unsafe_allow_html=True)
        link = f"https://arxiv.org/pdf/{prediction[str(i)][2]}.pdf"
        st.write(f"link [here]({link})")
    end_time = time.time()
    #st.write('time to query')
    #end_time - start_time

#st.write(
#f"<h1 style='text-align: left; color: #ABB2B9; font-size: 15px;'>{test_df.iloc[i,2]}</h1>",
#unsafe_allow_html=True)
