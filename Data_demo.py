import streamlit as st
import snowflake.connector
import snowflake-connector-python
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

# Use the search term to perform a SQL query on the Snowflake database
if search_term:
    # Perform the SQL query
    cursor = conn.cursor()
    query = f"SELECT * FROM CUSTOMER WHERE C_NAME LIKE '%{search_term}%'"
    cursor.execute(query)
    results = cursor.fetchall()
    
    # Display the results as a table
    if results:
        df = pd.DataFrame(results, columns=['C_MKTSEGMENT', 'C_PHONE', 'C_ACCTBAL', 'C_ADDRESS', 'C_NATIONKEY', 'C_CUSTKEY', 'C_NAME', 'C_COMMENT'])
        st.write(df)
        
        # Create a bar chart of the results
        chart = alt.Chart(df).mark_bar().encode(
            x='C_NAME',
            y='C_ACCTBAL'
        ).properties(
            width=600,
            height=400
        )
        st.altair_chart(chart, use_container_width=True)
        
    else:
        st.write("No results found.")
