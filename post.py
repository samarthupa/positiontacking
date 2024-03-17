import streamlit as st
from googlesearch import search

def track_position(domain, keyword):
    try:
        position = 1
        for url in search(keyword, stop=100, pause=2):
            if domain in url:
                return position
            position += 1
        return "Not found in the top 100 results"
    except Exception as e:
        return f"Error: {e}"

def main():
    st.title("Position Tracking Tool")

    domain = st.text_input("Enter your domain:")
    keyword = st.text_input("Enter your keyword:")

    if st.button("Track Position"):
        if domain and keyword:
            position = track_position(domain, keyword)
            st.write(f"The position of {domain} for the keyword '{keyword}' is: {position}")
        else:
            st.warning("Please enter both a domain and a keyword.")

if __name__ == "__main__":
    main()
