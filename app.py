import streamlit as st
import requests
import pandas as pd
import random
import time


api_url = 'https://literaturereview-z37yi6v7za-ew.a.run.app'
api_local = 'http://127.0.0.1:8000/predict'
st.set_page_config(
    page_title="Automated Literature Review",  # => Quick reference - Streamlit
    page_icon="📚",
    layout="wide",  # wide
    initial_sidebar_state="auto")  # collapsed

## setup for sidebar ##
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

## setup main ##
st.markdown(
    "<h1 style='text-align: center; color: #5D6D7E;'>an automated literature review tool</h1>",
    unsafe_allow_html=True)
## setup search bar ##

#dirname = os.path.dirname(__file__)
#filename = os.path.join(dirname, 'raw_data/trimmed_arxiv_docs5000.csv')
#
filename = 'https://storage.googleapis.com/wagon-data-735-vianadeabreu/data/trimmed_arxiv_docs5000.csv'
start_time = time.time()


test_df = pd.read_csv(filename)
end_time = time.time()
end_time - start_time

#search bar
#title = st.text_input('','search')
#st.button(label='Enter', key=None, help=None, on_click=None, args=None, kwargs=None)
#if st.button('click me'):
# print is visible in the server output, not in the page
#if title in list(test_df['title']):
#   st.write('Related papers:',
#search.run_search(n_neighbors=option+1)[title])
#else:
#   st.write('Paper does not exist')
#st.write('You look for the cluster: ', main.run_main(title))
#option = st.slider('Select number of related papers to show', 1, 10, 3)


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

#icon("search")
input_user = st.text_input("", "search...")
neighbors = st.number_input(
    '',
    min_value=2,
    max_value=30,
)
button_clicked = st.button("OK")

params = {'user_input': input_user.split(), 'neighbors': neighbors}

if button_clicked:
    params
    response = requests.get(api_local, params=params)
    #response.text
    prediction = response.json()
    #prediction
    indices = prediction['indices']
    #result = main.run_main(input_user, neighbors)
    indices = random.sample(range(0, test_df.shape[0]), k=neighbors)
    st.write(
        f"<h1 style='text-align: left; color: #5D6D7E; font-size: 18px;'>Sorry, we are under construction! But here are {neighbors} nice papers to read:</h1>",
        unsafe_allow_html=True)
    for i in indices:
        st.write(
            f"<h1 style='text-align: left; color: #ABB2B9; font-size: 15px;'>{test_df.iloc[i,2]}</h1>",
            unsafe_allow_html=True)
        st.write(
            f"<h1 style='text-align: left; color: #ABB2B9; font-size: 15px; font-style: italic;'>{test_df.iloc[i,5]}</h1>",
            unsafe_allow_html=True)
        link = f"https://arxiv.org/pdf/{test_df.iloc[i,0]}.pdf"
        st.write(f"link [here]({link})")
