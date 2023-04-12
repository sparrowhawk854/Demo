import streamlit as st

# Set the title of the app
st.title("Data Talk")

# Add a text input for the user to search
search_term = st.text_input("Enter a search term")

# Use the search term to perform some action, such as querying a database or API
if search_term:
    # Perform some action with the search term
    st.write("You searched for:", search_term)
