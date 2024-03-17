import requests
import streamlit as st

def fetch_google_search_results(api_key, cx, query):
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        search_results = response.json()
        return search_results
    else:
        st.error("Failed to fetch search results. Please try again later.")
        return None

def main():
    st.title("Google SERP Top 10 Results Finder")

    api_key = st.text_input("Enter your Google Custom Search API Key:")
    cx = st.text_input("Enter your Custom Search Engine ID (CX):")
    keyword = st.text_input("Enter your keyword to search:")

    if st.button("Search"):
        if not api_key or not cx or not keyword:
            st.warning("Please fill in all the fields.")
        else:
            search_results = fetch_google_search_results(api_key, cx, keyword)
            if search_results:
                search_info = search_results.get('searchInformation', {})
                if 'formattedTotalResults' in search_info:
                    st.subheader(f"Total Results: {search_info['formattedTotalResults']}")
                else:
                    st.subheader("Total Results: Not Available")

                search_parameters = search_results.get('queries', {}).get('request', [])
                for param in search_parameters:
                    if 'title' in param:
                        st.write(f"Search Term: {param['title']}")
                    if 'country' in param:
                        st.write(f"Region: {param['country']}")
                    if 'language' in param:
                        st.write(f"Language: {param['language']}")

                applied_filters = search_results.get('searchInformation', {}).get('spelling', {})
                if applied_filters:
                    st.write(f"Applied Filters: {applied_filters}")

                search_items = search_results.get('items', [])
                if search_items:
                    st.subheader("Top 10 Search Results:")
                    for idx, result in enumerate(search_items, start=1):
                        st.write(f"{idx}. {result['title']}: {result['link']}")
            else:
                st.info("No results found for the given keyword.")

if __name__ == "__main__":
    main()
