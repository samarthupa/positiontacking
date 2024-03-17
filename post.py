import streamlit as st
import requests

# Placeholders for your Programmable Search Engine credentials
CX = "YOUR_PROGRAMMABLE_SEARCH_ENGINE_ID"
API_KEY = "YOUR_API_KEY"

def fetch_results(keyword):
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX}&q={keyword}"
    response = requests.get(url)

    try:
        data = response.json()
        results = data.get("items", [])[:10]  # Get top 10 results

        # Display results with position and link (Option 1: Separate link construction)
        st.write("**SERP Results for:**", keyword)
        for i, result in enumerate(results):
            link = f"https://en.cppreference.com/w/cpp/types/result_of}]({result['link']})"
            st.write(f"**Position {i+1}:**\n{link}")

        # Alternatively, use string formatting (Option 2: Older Python versions)
        # for i, result in enumerate(results):
        #     link = "https://en.cppreference.com/w/cpp/types/result_of}]({})".format(result['link'])
        #     st.write("**Position {}:**\n{}".format(i+1, link))
    except Exception as e:
        st.error("An error occurred while fetching results:", e)
        st.write("Please check your API credentials and internet connection.")

# Streamlit app layout
st.title("Google SERP Crawler")
keyword = st.text_input("Enter Keyword")

if st.button("Search"):
    fetch_results(keyword)
