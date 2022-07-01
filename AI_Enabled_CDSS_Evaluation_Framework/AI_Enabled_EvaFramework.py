import streamlit as st

import questionnaire_amharic
import questionnaire_english

st.set_page_config(layout="wide")


def main():
    st.title("AI-Enabled CDSS Evaluation Framework: Customized Version")
    st.sidebar.title("AI-Enabled CDSS Evaluation Framework")
    languageChoice = st.sidebar.selectbox("Select your preferred language ", ['Amharic', 'English'])

    if languageChoice == 'English':
        questionnaire_english.main()
    else:
        questionnaire_amharic.main()


if __name__ == '__main__':
    main()
    hide_streamlit_style = """
                <style>
                # MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                footer:after {
                    content:'Powered by ETRO-VUB, JU, and NASCERE';
    	            visibility: visible;
    	            display: block;
    	            position: relative;
    	            # background-color: red;
    	            padding: 5px;

                }

                </style>
                """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
