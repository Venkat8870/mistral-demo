import streamlit as st

# Set page title
st.title("ASML AI Board")

# Add search button as per user story MP-3
search_query = st.text_input("Search", "")
if st.button("Search"):
    if search_query:
        st.write(f"Searching for: {search_query}")
        # Here you would add the actual search functionality
        # For now, it just displays what would be searched
    else:
        st.warning("Please enter a search term")