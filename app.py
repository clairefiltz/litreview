import streamlit as st
import numpy as np
import pandas as pd
from litreview.data import search, main
import os
st.set_page_config(
    page_title="Automated Literature Review", # => Quick reference - Streamlit
    page_icon="🐍",
    layout="wide", # wide
    initial_sidebar_state="auto") # collapsed


## setup for sidebar ##
sideb = st.sidebar
sideb.image("images/logo.png", use_column_width=True)
sideb.markdown(
    "<h1 style='text-align: center; color: #5D6D7E;'>Demo Day - Batch 735 - Berlin</h1>",
    unsafe_allow_html=True
)
sideb.write(
    "<h1 style='text-align: center; color: #5D6D7E; font-size: 13px;'>Claire Filtz, Felix Wohlleben</h1>",
    unsafe_allow_html=True
)
sideb.write(
    "<h1 style='text-align: center; color: #5D6D7E; font-size: 13px;'>Issa Al Barwani, Alex Viana</h1>",
    unsafe_allow_html=True
)

## setup main ##
st.markdown(
    "<h1 style='text-align: center; color: #5D6D7E;'>An Automated Literature Review Tool</h1>",
    unsafe_allow_html=True
)
## setup search bar ##


#dirname = os.path.dirname(__file__)
#filename = os.path.join(dirname, 'raw_data/trimmed_arxiv_docs5000.csv')
#
#filename = 'https://storage.googleapis.com/wagon-data-735-vianadeabreu/data/trimmed_arxiv_docs5000.csv'
#test_df = pd.read_csv(filename)



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

icon("search")
input_user = st.text_input("", "search...")
neighbors = st.number_input('',
    min_value=2,
    max_value=30,
)
button_clicked = st.button("OK")

if button_clicked:
    result = main.run_main(input_user, neighbors)
    st.write(
        "<h1 style='text-align: left; color: #5D6D7E; font-size: 18px;'>Related papers:</h1>",
        unsafe_allow_html=True)
    for paper in result:
        st.write(
            f"<h1 style='text-align: left; color: #ABB2B9; font-size: 15px;'>{paper[0]}</h1>",
            unsafe_allow_html=True)
