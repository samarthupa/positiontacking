import requests
import streamlit as st
import pandas as pd

# Function to fetch SERP data using the Custom Search JSON API
def fetch_serp_data(api_key, cx, keyword, domain):
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={keyword}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Parse the data to find the ranking position of the domain
        for index, item in enumerate(data.get('items', []), start=1):
            if domain.lower() in item.get('link', '').lower():
                return index
    return None

# Streamlit app layout
def main():
    st.title('Google SERP Position Tracker')
    st.write('Enter your domain and keywords to track their positions in Google search results.')

    # Input fields for domain and multiple keywords
    domain = st.text_input('Enter your domain:')
    keywords = st.text_area('Enter your keywords (one per line):')

    api_key = "AIzaSyCLrD3sJw3PiSkVjFtvsesI8tbS5uAu7xc"
    cx = "67746a8fc42004079"

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
                ranking_position = fetch_serp_data(api_key, cx, keyword, domain)
                if ranking_position is not None:
                    results.append({'Keyword': keyword, 'Ranking Position': ranking_position})
                else:
                    results.append({'Keyword': keyword, 'Ranking Position': 'Not found'})

            # Convert the list of dictionaries to a DataFrame
            results_df = pd.DataFrame(results)

            # Display results in a table
            st.write(results_df)

if __name__ == '__main__':
    main()
