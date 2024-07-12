import streamlit as st

def main():
    # Get the current page
    page = st.experimental_get_query_params().get("page", ["English"])[0]

    # Define the pages with title, about, description, and how_to_use
    pages = {
        "English": {
            "title": "PAMiLYA: Philippine Family Law Chatbot - Empowering Access to Legal Help",
            "about": "About the App",
            "description": "In the Philippines, many underprivileged families face legal issues but cannot readily afford the high costs associated with legal assistance. PAMiLYA, a database of family relations related legal cases and resolutions, aims to bridge this gap. It offers free and accessible pre-legal consultation related to family law, aiding families, students, lawmakers, law enforcers, societal organizations, and law enthusiasts in gaining awareness and understanding of Philippine Family Law. This initiative also aims to assist Barangay officials or LGU units in providing necessary legal counsel to resolve family conflicts or disputes. PAMiLYA seeks to empower families and communities by providing clear, understandable guidance on their rights and legal options.",
            "how_to_use": """
            Insert your instructions or guide on how to use the app here.
            You can use Markdown for formatting:
            - Bullet 1
            - Bullet 2
            """,
            "limitations": "sample limitations"
        },
        "Filipino": {
            "title": "PAMiLYA: Chatbot para sa Philippine Family Law - Pinapaigtingin Makamit ang Tulong Legal",
            "about": "Tungkol sa App",
            "description": "Sa Pilipinas, maraming pamilyang mahihirap ang hinaharap ang mga isyung legal ngunit hindi agad makakaya ang mataas na gastos na kaakibat ng tulong legal. Ang PAMiLYA, isang database ng mga kaso at resolusyon sa batas pamilya, ay nilikha upang punan ang agwat na ito. Nag-aalok ito ng libre at abot-kayang konsultasyon bago mag-legal na nauugnay sa batas pamilya, tumutulong sa mga pamilya, mag-aaral, mga mambabatas, mga tagapagtupad ng batas, mga organisasyon sa lipunan, at mga tagahanga ng batas na maunawaan ang batas pamilya sa Pilipinas. Layunin din nito ang pagtulong sa mga opisyal ng Barangay o mga yunit ng LGU sa pagbibigay ng kaukulang payo legal upang lutasin ang mga alitan o labanang pamilya. Ang PAMiLYA ay layuning palakasin ang mga pamilya at komunidad sa pamamagitan ng malinaw at maaunawaang patnubay tungkol sa kanilang mga karapatan at legal na mga pagpipilian.",
            "how_to_use": """
            Ilagay ang mga tagubilin o gabay kung paano gamitin ang app dito.
            Pwede kang gumamit ng Markdown para sa pag-format:
            - Tuldok 1
            - Tuldok 2
            """,
            "limitations": "sample limitations"
        }
    }

    # Sidebar to select the page
    page_selection = st.sidebar.radio("Select Page", list(pages.keys()), index=list(pages.keys()).index(page))
    st.experimental_set_query_params(page=page_selection)

    # Display the selected page content
    st.title(pages[page_selection]["title"])
    st.header(pages[page_selection]["about"])
    st.write(pages[page_selection]["description"])
    st.header('Paano Gamitin ang App')
    st.write(pages[page_selection]["how_to_use"])
    st.header('Limitasyon ng App')
    st.write(pages[page_selection]["limitations"])

    # Citations in small letters at the bottom
    st.sidebar.markdown('**Citations**')
    st.sidebar.write("UST Faculty. (2021). Persons and Family Relations. Retrieved from https://www.ustcivillaw.com/wp-content/uploads/2021/08/Persons-and-Family-Relations_HVNj62YQuGoFTpNVUVNb.pdf")

if __name__ == "__main__":
    main()


