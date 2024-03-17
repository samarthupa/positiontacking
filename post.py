import requests
import streamlit as st

# Function to fetch SERP data using the Custom Search JSON API
def fetch_serp_data(api_key, cx, keyword, domain):
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={keyword}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Parse the data to find the ranking position of the domain
        for index, item in enumerate(data.get('items', []), start=1):
            if domain in item.get('link', ''):
                return index
    return None

# Streamlit app layout
def main():
    st.title('Google SERP Position Tracker')
    st.write('Enter your domain and keyword to track its position in Google search results.')

    # Input fields for domain, keyword, and API key
    domain = st.text_input('Enter your domain:')
    keyword = st.text_input('Enter your keyword:')
    api_key = "AIzaSyCLrD3sJw3PiSkVjFtvsesI8tbS5uAu7xc"
    cx = "67746a8fc42004079"

    if st.button('Track Position'):
        if not domain or not keyword:
            st.error('Please fill in both domain and keyword.')
        else:
            # Call function to fetch SERP data
            ranking_position = fetch_serp_data(api_key, cx, keyword, domain)
            if ranking_position:
                st.success(f'Your domain "{domain}" is ranking at position {ranking_position} for keyword "{keyword}".')
            else:
                st.error(f'Your domain "{domain}" is not found in the search results for keyword "{keyword}".')

if __name__ == '__main__':
    main()
