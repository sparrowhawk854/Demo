

import streamlit as st
import snowflake.connector

import pandas as pd
import altair as alt

# Set up Snowflake connection
conn = snowflake.connector.connect(
    user='Hamburger',
    password='NumNumNum99',
    #account='australia-east.azure/pt11496',
    account='app.snowflake.com/australia-east.azure/pt11496',
    warehouse='COMPUTE_WH',
    database='SNOWFLAKE_SAMPLE_DATA',
    schema='TPCH_SF1'
)

# Set the title of the app
st.title("Hamburgler")

# Add a text input for the user to search
search_term = st.text_input("Enter a search term")

