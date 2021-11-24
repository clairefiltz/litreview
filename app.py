import streamlit as st
import numpy as np
import pandas as pd
from litreview.data import search

st.set_page_config(
    page_title="Automated Literature Review", # => Quick reference - Streamlit
    page_icon="🐍",
    layout="wide", # wide
    initial_sidebar_state="auto") # collapsed


CSS = """
h1 {
    color: orange;
}
.stApp {
    background-image: url(https://image.freepik.com/free-photo/old-books-with-white-background-copy-space_23-2148898330.jpg);
    background-size: cover;
    background-color: transparent;
    opacity:0.5
}
"""

if st.checkbox('Inject CSS'):
    st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

st.markdown("""## An Automated Literature Review Tool
Welcome!
""")

file_path = 'gs://litreview-bucket/litreview-bucket/trimmed_arxiv_docs5000.csv'
test_df = pd.read_csv(file_path)

#search bar
title = st.text_input('Title of Paper', 'Please insert the name of a paper here')

#st.button(label='Enter', key=None, help=None, on_click=None, args=None, kwargs=None)
if st.button('click me'):
    # print is visible in the server output, not in the page
    if title in list(test_df['title']):
        st.write('Related papers:', search.run_search()[title])
    else:
        st.write('Paper does not exist')


#Enter button

#search.run_search()[title]



st.write('Here are the 10 most related papers to your input:')




test_df = pd.read_csv(file_path)
st.write(test_df[['authors', 'title', 'doi', 'category', 'abstract']].head(10))
