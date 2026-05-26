import streamlit as st
import pandas as pd
from io import BytesIO

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

# Add download report button as per user story MP-5
if st.button("Download Report"):
    # Generate sample report data
    report_data = {
        "Item": ["Item 1", "Item 2", "Item 3"],
        "Status": ["Active", "Active", "Active"],
        "Details": ["Sample item 1", "Sample item 2", "Sample item 3"]
    }
    
    # Create DataFrame
    df = pd.DataFrame(report_data)
    
    # Convert to CSV
    csv = df.to_csv(index=False)
    
    # Download button
    st.download_button(
        label="Click to Download CSV Report",
        data=csv,
        file_name="asml_ai_report.csv",
        mime="text/csv"
    )
    
    # Show preview
    st.subheader("Report Preview")
    st.dataframe(df)

# Add remove button as per user story MP-4
st.subheader("Items")
# Sample list of items (in a real app, this would come from your data source)
items = ["Item 1", "Item 2", "Item 3"]

# Display items with remove buttons
for i, item in enumerate(items):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.write(item)
    with col2:
        if st.button(f"Remove", key=f"remove_{i}"):
            # In a real app, you would remove the item from your data source
            st.success(f"Removed: {item}")
            # For demo purposes, we'll just show a success message