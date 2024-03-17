import requests
import streamlit as st
import pandas as pd
import urllib.parse

# Function to fetch SERP data using the Custom Search JSON API
def fetch_serp_data(api_key, cx, keyword, domain):
    # Encode the domain to handle special characters
    encoded_domain = urllib.parse.quote(domain)
    # Construct the URL to request mobile search results
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={keyword}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Parse the data to find the top 10 search results
        search_results = []
        for item in data.get('items', [])[:10]:
            search_results.append({'Title': item.get('title', ''), 'URL': item.get('link', '')})
        return search_results
    return None

# Streamlit app layout
def main():
    st.title('Google SERP Position Tracker')
    st.write('Enter your domain and keywords to track their positions in Google search results.')

    # Input fields for domain and multiple keywords
    domain = st.text_input('Enter your domain:')
    keywords = st.text_area('Enter your keywords (one per line):')

    api_key = "AIzaSyCLrD3sJw3PiSkVjFtvsesI8tbS5uAu7xc"
    cx = "622c52b5ab94d4629"

    if st.button('Track Positions'):
        if not domain or not keywords:
            st.error('Please fill in both domain and keywords.')
        else:
            # Split keywords by line and remove empty lines
            keyword_list = [keyword.strip() for keyword in keywords.split('\n') if keyword.strip()]

            # Initialize an empty list to store the results
            results = []

            # Fetch SERP data for each keyword
            for keyword in keyword_list:
                try:
                    search_results = fetch_serp_data(api_key, cx, keyword, domain)
                    if search_results is not None:
                        for rank, result in enumerate(search_results, start=1):
                            results.append({'Keyword': keyword, 'Rank': rank, 'Title': result['Title'], 'URL': result['URL']})
                    else:
                        results.append({'Keyword': keyword, 'Rank': 'Not found', 'Title': 'Not found', 'URL': 'Not found'})
                except Exception as e:
                    results.append({'Keyword': keyword, 'Rank': 'Error', 'Title': 'Error', 'URL': 'Error'})

            # Convert the list of dictionaries to a DataFrame
            results_df = pd.DataFrame(results)

            # Display results in a table
            st.write(results_df)

if __name__ == '__main__':
    main()
