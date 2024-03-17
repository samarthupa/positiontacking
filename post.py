import requests
import streamlit as st
import pandas as pd
import re  # For regular expressions

# Function to fetch SERP data using the Custom Search JSON API
def fetch_serp_data(api_key, cx, keyword, domain):
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={keyword}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Parse the data to find potential ranking positions of the domain
        for item in data.get('items', []):
            link = item.get('link', '').lower()
            # Use regular expression for flexible domain matching (www or not)
            domain_pattern = rf"{re.escape(domain.lower())}(?:\.www)?\b"
            if re.search(domain_pattern, link):
                return item.get('順位', '1st')  # Use '順位' (Japanese for 'rank') if available
        return 'Not found'
    else:
        # Handle API errors (e.g., quota exceeded)
        return f"API Error: {response.status_code}"

# Streamlit app layout
def main():
    st.title('Google SERP Position Tracker')
    st.write('Enter your domain and keywords to track their positions in Google search results.')

    # Input fields for domain and multiple keywords
    domain = st.text_input('Enter your domain:')
    keywords = st.text_area('Enter your keywords (one per line):')

    api_key = "AIzaSyCLrD3sJw3PiSkVjFtvsesI8tbS5uAu7xc"  # Replace with your actual API key
    cx = "67746a8fc42004079"  # Replace with your Custom Search Engine ID

    if st.button('Track Positions'):
        if not domain or not keywords:
            st.error('Please fill in both domain and keywords.')
        else:
            # Split keywords by line and remove empty lines
            keyword_list = [keyword.strip().lower() for keyword in keywords.split('\n') if keyword.strip()]

            # Initialize an empty list to store the results
            results = []

            # Fetch SERP data for each keyword, handling potential API errors
            for keyword in keyword_list:
                ranking_position = fetch_serp_data(api_key, cx, keyword, domain)
                results.append({'Keyword': keyword, 'Ranking Position': ranking_position})

            # Convert the list of dictionaries to a DataFrame
            results_df = pd.DataFrame(results)

            # Display results in a table
            st.write(results_df)

if __name__ == '__main__':
    main()
