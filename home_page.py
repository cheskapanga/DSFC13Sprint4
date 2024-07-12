# import streamlit as st

# def main():
#     # Get the current page
#     page = st.experimental_get_query_params().get("page", ["English"])[0]

#     # Define the pages
#     pages = {
#         "English": {
#             "title": "PAMiLYA: Philippine Family Law Chatbot - Empowering Access to Legal Help",
#             "about": "About the App",
#             "description:": "In the Philippines, many underprivileged families face legal issues but cannot readily  afford the high costs associated with legal assistance. PAMiLYA is designed to bridge this gap, offering free and accessible pre-legal consultation related to family law. This chatbot aims to empower families and communities by providing clear, understandable guidance on their rights and legal options.",
#             "how_to_use": """
#             Insert your instructions or guide on how to use the app here.
#             You can use Markdown for formatting:
#             - Bullet 1
#             - Bullet 2
#             """
#         },
#         "Filipino": {
#             "title": "PAMiLYA - Philippine Family Law Chatbot",
#             "about": "Tungkol sa App",
#             "how_to_use": """
#             Ilagay ang mga tagubilin o gabay kung paano gamitin ang app dito.
#             Pwede kang gumamit ng Markdown para sa pag-format:
#             - Tuldok 1
#             - Tuldok 2
#             """
#         }
#     }

#     # Sidebar to select the page
#     page_selection = st.sidebar.radio("Home Page", list(pages.keys()), index=list(pages.keys()).index(page))
#     st.experimental_set_query_params(page=page_selection)

#     # Display the selected page content
#     st.title(pages[page_selection]["title"])
#     st.header(pages[page_selection]["about"])
#     st.write(pages[page_selection]["description"])
#     st.header('How to Use the App')
#     st.write(pages[page_selection]["how_to_use"])

#     # Citations in small letters at the bottom
#     st.sidebar.markdown('**Citations**')
#     st.sidebar.write("Insert your citations or references here.")

# if __name__ == "__main__":
#     main()


import streamlit as st

def main():
    # Get the current page
    page = st.experimental_get_query_params().get("page", ["English"])[0]

    # Define the pages with title, about, description, and how_to_use
    pages = {
        "English": {
            "title": "Title",
            "about": "About the App",
            "description": "This is a description of the app in English. Add details about its purpose, features, or any other relevant information.",
            "how_to_use": """
            Insert your instructions or guide on how to use the app here.
            You can use Markdown for formatting:
            - Bullet 1
            - Bullet 2
            """
        },
        "Filipino": {
            "title": "Pamagat",
            "about": "Tungkol sa App",
            "description": "Ito ang paglalarawan ng app sa Filipino. Ilagay ang mga detalye tungkol sa layunin, mga feature, o anumang iba pang mahalagang impormasyon.",
            "how_to_use": """
            Ilagay ang mga tagubilin o gabay kung paano gamitin ang app dito.
            Pwede kang gumamit ng Markdown para sa pag-format:
            - Tuldok 1
            - Tuldok 2
            """
        }
    }

    # Sidebar to select the page
    page_selection = st.sidebar.radio("Select Page", list(pages.keys()), index=list(pages.keys()).index(page))
    st.experimental_set_query_params(page=page_selection)

    # Display the selected page content
    st.title(pages[page_selection]["title"])
    st.header(pages[page_selection]["about"])
    st.write(pages[page_selection]["description"])  # Added description here
    st.subheader('How to Use the App')
    st.write(pages[page_selection]["how_to_use"])

    # Citations in small letters at the bottom
    st.sidebar.markdown('**Citations**')
    st.sidebar.write("Insert your citations or references here.")

if __name__ == "__main__":
    main()


