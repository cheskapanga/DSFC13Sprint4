import streamlit as st

def main():
    # Title in large letters
    st.title('Title')

    # About the app in medium letters
    st.header('About the App')

    # How to use the app in slightly smaller letters
    st.subheader('How to Use the App')

    # Add your instructions or guide on how to use the app
    st.write("""
    Insert your instructions or guide on how to use the app here.
    You can use Markdown for formatting:
    - Bullet 1
    - Bullet 2
    """)

    # Citations in small letters at the bottom
    st.sidebar.markdown('**Citations**')
    st.sidebar.write("Insert your citations or references here.")

if __name__ == "__main__":
    main()
