import streamlit as st

from st_aggrid import AgGrid
# for-  Columns can be pinned, grouped and aggregated
from st_aggrid.grid_options_builder import GridOptionsBuilder

# from datetime import datetime, date, time

import pandas as pd

import os


surveyValue = {'fullname': [],
               'started at': [],
               'learnability': [],
               'operability': [],
               'user_interface': [],
               'data_entry': [],
               'advice_to_display': [],
               'legibility': [],
               'response_time': [],
               'stability': [],
               'security': [],
               'cp_performance': [],
               'change_in_order_behavior': [],
               'change_in_cp': [],
               'effectiveness': [],
               'overall_usefulness': [],
               'adherence_to_standards': [],
               'medical_quality': [],
               'user_knowledge_and_skills': [],
               'usage': [],
               'expectations_confirmation': [],
               'satisfaction_of_over_quality': [],
               'overall_satisfaction': [],
               'intension_to_use': [],
               'ends at': []}


def learnability():
    st.info("1. Learnability")
    learnability = "I'm satisfied with WEB-APP. I can quickly (i.e. without taking time) learn how to use it and begin doing some work with it."
    return learnability


def operability():
    st.info("2. Operability")
    operability = "I'm satisfied with the amount of effort and time required for the WEB-APP to operate and perform tasks correctly."
    return operability


def user_interface():
    st.info("3. User Interface")
    user_interface = "The WEB-APP allows users to easily navigate through the user interfaces (UI) and deliver the results in the correct format. In addition, the WEB-APP provides appropriate controls, menus, and outputs. "

    return user_interface


def data_entry():
    st.info("4. Data Entry \n")
    data_entry = "The WEB-APP provides a simple and consistent data entry interface. The WEB-APP enables the user to choose a specific task and encourages minimum data entry and steps through the use of selection boxes, wizards, and other features."
    return data_entry


def advice_to_display():
    st.info("5. Advice to display")
    advice_to_display = "I am satisfied with the advice to display. It refers to the WEB-APP making recommendations to the user, and the users are expected to make their own decisions and overruling WEB-APP recommendations they believe to be inappropriate."
    return advice_to_display


def legibility():
    st.info("6. Legibility")
    legibility = "I am satisfied how WEB-APP and its decisions are understood by non-AI experts."
    return legibility


def response_time():
    st.info("7. Response time")
    response_time = "I am satisfied with the response time i.e. it refers to the time taken to transmit the inquiry, process it by WEB-APP, and transmit the response back to the user."
    return response_time


def stability():
    st.info("8. Stability")
    stability = "I am satisfied with the WEB-APP sessions that are crash-free, i.e. as effectively the system handles exceptions and errors."
    return stability


def security():
    st.info("9. Security")
    security = "I am satisfied with the capability of WEB-APP to protect information and data so that unauthorized persons or systems cannot read or modify them and authorized persons or systems are not denied access."
    return security


def cp_performance():
    st.info("10. CP Performance")
    cp_performance = "The WEB-APP enables me to execute activities with appropriate evidence and within acceptable time frames. The WEB-APP makes it easier and more convenient to gather evidence than paper-based clinical guidelines, point-of-care instruments, card-sheet, and so on."
    return cp_performance


def change_in_order_behavior():
    st.info("11. Change in order behavior")
    change_in_order_behavior = "I am satisfied with the the capability of WEB-APP allowing for real time-based interactions between the user and the WEB-APP recommendations."
    return change_in_order_behavior


def change_in_cp():
    st.info("12. Change in CP")
    change_in_cp = "The evidence that I got from the WEB-APP is diverse enough and important. The result of using the system are apparent to me."
    return change_in_cp


def effectiveness():
    st.info("13. Effectiveness")
    effectiveness = "I am satisfied with the way WEB-APP speeds up workflow and displays the desired output as the user expecst, so that a user can complete tasks accurately and completely in a specified context?"
    return effectiveness


def overall_usefulness():
    st.info("14. Overall usefulness")
    overall_usefulness = "Overall, I found the WEB-APP tool was useful. i.e. it refers to the quality of WEB-APPbeing useful under different contextual factors."
    return overall_usefulness


def adherence_to_standards():
    st.info("15. Adherence to standards")
    adherence_to_standards = "The evidence that I got from WEB-APPadheres to standards  i.e. quality of WEB-APP abiding/ sticking by both industry regulations and government legislations"
    return adherence_to_standards


def medical_quality():
    st.info("16. Medical quality")
    medical_quality = "The quality of evidence that I got from the WEB-APP instrument is high and important "
    return medical_quality


def user_knowledge_and_skills():
    st.info("17. User knowledge and skills")
    Learnability = "WEB-APP assists or increases the likelihood of desired clinical outcomes and is consistent with current professional knowledge and skills."
    return Learnability


def usage():
    st.info("18. Usage")
    usage = "My experience with WEB-APP didn’t face any problem "
    return usage


def expectations_confirmation():
    st.info("19. Expectations confirmation")
    expectations_confirmation = "I found WEB-APP performed as expected based on my prior experience and/or expectations."
    return expectations_confirmation


def satisfaction_of_over_quality():
    st.info("20. Satisfaction of over  quality")
    satisfaction_of_over_quality = "I am satisfied with the overall  WEB-APP's system, service (in finding referral and treatable cases), and information output quality."
    return satisfaction_of_over_quality


def overall_satisfaction():
    st.info("21. Overall satisfaction")
    overall_satisfaction = "Overall I’m satisfied with WEB-APP i.e. the affective reactions of users toward the use of WEB-APP in general."
    return overall_satisfaction


def intension_to_use():
    st.info("22. Intension to use")
    intension_to_use = "I intend to use the system for my routine duty to perform my job. Given that I have access to WEB-APP for my routine duty, I predict that I would adopt it."
    return intension_to_use


def create_interactive_df(data):
    """
    A function to create an interactive and seelectable dataframe
    """
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_pagination(paginationAutoPageSize=True)  # Add pagination
    gb.configure_side_bar()  # Add a sidebar
    gb.configure_selection('multiple', use_checkbox=True,
                           groupSelectsChildren="Group checkbox select children")  # Enable multi-row selection
    gridOptions = gb.build()

    grid_response = AgGrid(
        data,
        gridOptions=gridOptions,
        data_return_mode='AS_INPUT',
        update_mode='MODEL_CHANGED',
        fit_columns_on_grid_load=False,
        theme='blue',  # Add theme color to the table
        enable_enterprise_modules=True,
        height=350,
        # width='100%',
        reload_data=True
    )

    data = grid_response['data']
    selected = grid_response['selected_rows']
    df = pd.DataFrame(selected)  # Pass the selected rows to a new dataframe df
    return df


def get_detailed_feedback(evalutation_df):
    neutralResults = evalutation_df.where(
        evalutation_df == 'Neutral').stack().index.tolist()
    StronglyDisagreeResults = evalutation_df.where(
        evalutation_df == 'Strongly Disagree').stack().index.tolist()
    DisagreeResults = evalutation_df.where(
        evalutation_df == 'Disagree').stack().index.tolist()
    # rslt_Disagree = evalutation_df[evalutation_df[col] == 'Disagree (በጣም አልስማማም)']
    # rslt_neutral = evalutation_df[evalutation_df[col] == 'Neutral (ገለልተኛ)']
    st.write("Neutral", neutralResults)
    st.write("Strongly Disagree", StronglyDisagreeResults)
    st.write("Disagree", DisagreeResults)


def main():
    """questionnairee web form"""
    st.info("The AI-Enabled CDSS questionnaire form is based on Ji, Mengting, et al. 2021 paper  and is customized to our requirements.")

    st.success("Please complete the questionnairee form after using the CDS POC WEB_APP")
    fullname = st.text_input('Evaluator Full Name')

    evalutation_started_time = st.time_input('Evaluation started  time')

    # timestamp = pd.Timestamp(datetime.today())
    # timestamp = datetime.datetime.now()
    # evalutation_started_time = st.write(
    # 'Evaluation started:', 'Hour:', timestamp.hour, 'Minute:', timestamp.minute, 'Second:', timestamp.second)

    reviewerResponseChoice = ['',
                              'Strongly Agree',
                              'Agree',
                              'Neutral',
                              'Disagree',
                              'Strongly Disagree',

                              # 'Comment in the case of neutral, disagree and strongly disagree (“ገለልተኛ፣ አልስማማም እና በጣም አልስማማም” በሚለው ጉዳይ ላይ አስተያየት ይስጡ)'
                              ]
    # making the orientaiton horizontal
    # st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    with st.expander(label="Perceived Ease of Use"):
        learnability_Response = st.selectbox(learnability(), reviewerResponseChoice)
        operability_Response = st.selectbox(operability(), reviewerResponseChoice)
        user_interface_Response = st.selectbox(user_interface(), reviewerResponseChoice)
        data_entry_Response = st.selectbox(data_entry()+"\n", reviewerResponseChoice)
        advice_to_display_Response = st.selectbox(advice_to_display()+"\n", reviewerResponseChoice)
        legibility_Response = st.selectbox(legibility(), reviewerResponseChoice)

    with st.expander(label="System Quality "):
        response_time_Response = st.selectbox(response_time(), reviewerResponseChoice)
        stability_Response = st.selectbox(stability(), reviewerResponseChoice)
    with st.expander(label="Information Quality "):
        security_Response = st.selectbox(security(), reviewerResponseChoice)
        cp_performance_Response = st.selectbox(cp_performance(), reviewerResponseChoice)

    with st.expander(label="Decision Changes  "):
        change_in_order_behavior_Response = st.selectbox(
            change_in_order_behavior(), reviewerResponseChoice)
        change_in_cp_Response = st.selectbox(change_in_cp(), reviewerResponseChoice)

    with st.expander(label="Process Changes"):
        effectiveness_Response = st.selectbox(effectiveness(), reviewerResponseChoice)
        overall_usefulness_Response = st.selectbox(overall_usefulness(), reviewerResponseChoice)
        adherence_to_standards_Response = st.selectbox(
            adherence_to_standards(), reviewerResponseChoice)
        medical_quality_Response = st.selectbox(medical_quality(), reviewerResponseChoice)
        user_knowledge_and_skills_Response = st.selectbox(
            user_knowledge_and_skills(), reviewerResponseChoice)

    with st.expander(label="Acceptance "):
        usage_Response = st.selectbox(usage(), reviewerResponseChoice)
        expectations_confirmation_Response = st.selectbox(
            expectations_confirmation(), reviewerResponseChoice)
        satisfaction_of_over_quality_Response = st.selectbox(
            satisfaction_of_over_quality(), reviewerResponseChoice)
        overall_satisfaction_Response = st.selectbox(overall_satisfaction(), reviewerResponseChoice)
        intension_to_use_Response = st.selectbox(intension_to_use(), reviewerResponseChoice)
    evalutation_ended_time = st.time_input('Evaluation ends at')

    with st.expander(label="Validate and Review the Response"):
        # AgGrid(evalutation_df)
        surveyValue = {'fullname': [fullname],
                       'started at': [evalutation_started_time],
                       'learnability': [learnability_Response],
                       'operability': [operability_Response],
                       'user_interface': [user_interface_Response],
                       'data_entry': [data_entry_Response],
                       'advice_to_display': [advice_to_display_Response],
                       'legibility': [legibility_Response],
                       'response_time': [response_time_Response],
                       'stability': [stability_Response],
                       'security': [security_Response],
                       'cp_performance': [cp_performance_Response],
                       'change_in_order_behavior': [change_in_order_behavior_Response],
                       'change_in_cp': [change_in_cp_Response],
                       'effectiveness': [effectiveness_Response],
                       'overall_usefulness': [overall_usefulness_Response],
                       'adherence_to_standards': [adherence_to_standards_Response],
                       'medical_quality': [medical_quality_Response],
                       'user_knowledge_and_skills': [user_knowledge_and_skills_Response],
                       'usage': [usage_Response],
                       'expectations_confirmation': [expectations_confirmation_Response],
                       'satisfaction_of_over_quality': [satisfaction_of_over_quality_Response],
                       'overall_satisfaction': [overall_satisfaction_Response],
                       'intension_to_use': [intension_to_use_Response],
                       'ends at': [evalutation_ended_time]
                       }
        evalutation_df = pd.DataFrame.from_dict(surveyValue)
        create_interactive_df(evalutation_df)

    if st.button('Submit'):
        # get the endrosed cp current directory
        current_directory = os.getcwd()
        filename = "/EvaluationResult.csv"
        # merge the file name to get the full paths
        Saved_Evaluation_Path = current_directory + filename
        if os.path.isfile(Saved_Evaluation_Path):
            evalutation_df.to_csv(Saved_Evaluation_Path, mode='a',  header=False)
        else:
            evalutation_df.to_csv(Saved_Evaluation_Path)
        st.success("The evaluation result is saved and submitted successfully")
        st.info("However, based on the results of the evaluation, a thorough understanding of the following is required to aid in the further development of the WEB-APP. One-on-one detail interviews are essential for getting the genuine insight of the expert or evaluator.")
        get_detailed_feedback(evalutation_df)
        if st.button('Finish'):
            st.success("Thanks for the detailed feedback")


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
