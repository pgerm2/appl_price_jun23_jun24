import streamlit as st
import pandas as pd
import numpy as np


# #streamlit run stocks_AAPL.py

st.title('Apple Closing Price ')

DATE_COLUMN = 'date/time'


#Converting the date column into datetime isn’t a quick job either. 
#You don’t want to reload the data each time the app is updated – 
#luckily Streamlit allows you to cache the data.
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(('AAPL.csv'), nrows=nrows)
    
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')

# Load 253 rows of data into the dataframe.
data = load_data(253)

# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('June 2023 to June 2024')


chart_data = pd.read_csv("AAPL.csv")

st.line_chart(data=chart_data, x='Date', y='Close')




