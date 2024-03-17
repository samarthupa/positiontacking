import streamlit as st
import requests

# Placeholders for your Programmable Search Engine credentials
CX = "622c52b5ab94d4629"
API_KEY = "AIzaSyCLrD3sJw3PiSkVjFtvsesI8tbS5uAu7xc"

def fetch_results(keyword):
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX}&q={keyword}"
    response = requests.get(url)

    try:
        data = response.json()
        results = data.get("items", [])[:10]  # Get top 10 results

        # Display results with position and link
        st.write("**SERP Results for:**", keyword)
        for i, result in enumerate(results):
            link = f"[Position {i+1}: {result['link']}]"
            st.write(link)

    except Exception as e:
        st.error("An error occurred while fetching results:", e)
        st.write("Please check your API credentials and internet connection.")

# Streamlit app layout
st.title("Google SERP Crawler")
keyword = st.text_input("Enter Keyword")

if st.button("Search"):
    fetch_results(keyword)
