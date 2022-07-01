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
    st.info("1. የመማር ችሎታ (Learnability)")
    learnability = "በክሊኒካል መተግበሪያው(WEB-APP ) ተደስቻለሁ። በፍጥነት (ማለትም ጊዜ ሳልወስድ) እንዴት መጠቀም አንዳለብኝ በመማር  አንዳንድ ስራዎችን መስራት ችያለሁ።"
    return learnability


def operability():
    st.info("2. ተግባራዊነት (Operability)")
    operability = "ክሊኒካል መተግበሪያው (WEB-APP ) በሚፈለገው ጥረት እና ጊዜ  ስራዎችን በትክክል ለመስራት እና ለማከናወን በሚያደርገው አስተዋጵኦ ተደስቻለሁ።"
    return operability


def user_interface():
    st.info("3. የተጠቃሚ በይነገጽ (User Interface) ")
    user_interface = "የክሊኒካል መተግበሪያው (WEB-APP ) የተጠቃሚ  በይነገጽ (User Interface) ቀላል እና ወጥነት ያላቸው በመሆናቸው ተጠቃሚዎች  ክሊኒካል መተግበሪያውን በቀላሉ ማሰስ (navigate) እና ውጤቶችን በትክክለኛው ቅርጸት እንዲያቀርቡ ያስችላቸዋል። በተጨማሪም፣ ክሊኒካል መተግበሪያው ተገቢ ቁጥጥሮችን፣ ሜንዋችን እና መገላጫዋችን ያቀርባል።"

    return user_interface


def data_entry():
    st.info("4. የክሊኒካል መሪጃ   ማስገቢያ (Data Entry) \n")
    data_entry = "የክሊኒካል መተግበሪያው (WEB-APP) ቀላል፣ ወጥነት እና ተከታታይ ያለው የመሪጃ ማስገቢያ በይነገጽ ያቀርባል።  የክሊኒካል መተግበሪያው ተጠቃሚው ውሱን ና የተመረጡ ተግባራትን እንዲያከናውን ያስችለዋል።  የክሊኒካል መተግበሪያው ተጠቃሚው ውሱን ና የተመረጡ ተግባራትን እንዲያከናውን ማበረታታት፥ አነስተኛውን የመሪጃ ግብዓት የመጠቀም   እና  በምርጫ ሳጥኖች፣ ጠቋሚዎች እና ሌሎች ባህሪያትን ያበረታታል። "
    return data_entry


def advice_to_display():
    st.info("5. እገዛ  እንዲታይ መምከር (Advice to display )")
    advice_to_display = "የክሊኒካል መተግበሪያው (WEB-APP) በማሳየት በሚሰጠው ምክር  እና አማራጭ ተደስቻለሁ። የክሊኒካል መተግበሪያው (WEB-APP) ለተጠቃሚው ምክሮችን መስጠት, እና ተጠቃሚዎች የራሳቸውን ውሳኔ እንዲወስኑ እና ተገቢ አይደሉም ብለው ያመኑትን ምክሮችን መሻር  እንዲችሉ እንዲችሉ በሚሰጠው አማራጭ  ተደስቻለሁ።"
    return advice_to_display


def legibility():
    st.info("6. ተገቢነት (Legibility)")
    legibility = "የክሊኒካል መተግበሪያው (WEB-APP)  እና የሚሰጣቸው ዝርዝር ውጤቶች  የሰው ሰሪሽ አስተውሎት ባልሆኑ ባለሙያዎች  (non-AI experts)  በቀላሉ መሪዳት ስለሚቻሉ ተደስቻለሁ።"
    return legibility


def response_time():
    st.info("7. የምላሽ ሰአት (Response time)")
    response_time = "የክሊኒካል መተግበሪያው (WEB-APP)   ጥያቄውን ለማስተላለፍ የሚወስድበት ግዜ,  እና የምላሽ ሰዓት ተደስቻለሁ ። ማለትም የክሊኒካል መተግበሪያው (WEB-APP)  ጥያቄውን ለማስኬድ እና ምላሹን ለተጠቃሚው ለማስተላለፍ የወሰደውን ጊዜ ያመለክታል።"
    return response_time


def stability():
    st.info("8. ዘላቂነት ያለው (Stability)")
    stability = "የክሊኒካል መተግበሪያው (WEB-APP)  ዘላቂነት ያለው በመሆኑ ፣  መተግበሪያው ከብልሽት ነፃ በሆኑ  ስህተቶችን በብቃት መቆጣጠር ይችላል ።"
    return stability


def security():
    st.info("9. ደህንነት (Security)")
    security = "የክሊኒካል መተግበሪያው (WEB-APP) ያልተፈቀደላቸው ሰዎች መሪጃዎችን ማንበብ እና መቀየር እንዳይችሉ በማድረግ እና  ለመጠበቅ ባለው አቅም ተደስቻለሁ። "
    return security


def cp_performance():
    st.info("10. የሲፒ (CP)   አፈፃፀም ብቃት (CP Performance)")
    cp_performance = "የክሊኒካል መተግበሪያው (WEB-APP) ተግባራትን በተገቢው ማስረጃ እና ተቀባይነት ባለው የጊዜ ገደብ ውስጥ እንድፈጽም ያስችለኛል። የክሊኒካል መተግበሪያው በወረቀት ላይ ከተመሰረቱ ክሊኒካዊ መመሪያዎች (guidelines)፣ መሳሪያዎች፣ ካርድዎች (card-sheet)  እና ከመሳሰሉት ይልቅ ማስረጃዎችን ለመሰብሰብ ቀላል እና ምቹ ያደርገዋል።"
    return cp_performance


def change_in_order_behavior():
    st.info("11. የባህሪ ለውጥ (Change in order behavior)")
    change_in_order_behavior = "በተጠቃሚው እና በክሊኒካል መተግበሪያው (WEB-APP) ምክሮች መካከል ባለው በእውነተኛ ጊዜ (real time-based interactions) ላይ የተመሰረተ መስተጋብር ተደስቻለሁ።"
    return change_in_order_behavior


def change_in_cp():
    st.info("12. በ CP ውጤት ላይ ለውጥ (Change in CP)")
    change_in_cp = "ከክሊኒካል መተግበሪያው (WEB-APP) ያገኘሁት ማስረጃ በቂ፤ አካታች እና ጠቃሚ ናቸው። መተግበሪያውን መጠቀም ውጤቱ ለእኔ ግልጽ ነው።"
    return change_in_cp


def effectiveness():
    st.info("13. ውጤታማነት (Effectiveness)")
    effectiveness = "የክሊኒካል መተግበሪያው (WEB-APP) የስራ ሂደትን የሚያፋጥን እና ተጠቃሚው እንደሚጠብቀው የሚፈለገውን ውጤት በሚያሳይበት መንገድ ተደስቻለሁ፣ በዚህም ተጠቃሚው በትክክል እና በተወሰነ አውድ ውስጥ ስራዎችን ሙሉ በሙሉ ማጠናቀቅ እንዲችል ይሪዳዋል።"
    return effectiveness


def overall_usefulness():
    st.info("14. አጠቃላይ ጠቀሜታ(Overall usefulness)")
    overall_usefulness = "በአጠቃላይ፣ የክሊኒካል መተግበሪያው (WEB-APP)  ጠቃሚ ሆኖ አግኝቼዋለሁ። ማለትም የክሊኒካል መተግበሪያው በተለያዩ የአውድ ሁኔታዎች ስር ጠቃሚ መሆኑን ያመለክታል።"
    return overall_usefulness


def adherence_to_standards():
    st.info("15. ለመርህ መገዛት (Adherence to standards )")
    adherence_to_standards = "ከክሊኒካል መተግበሪያው (WEB-APP)   ያገኘሁት ማስረጃዎች  መርሆችን ያከበሩ ናቸው። ማለትም  ሁሉንም ደንቦችን እና ህጎችን ያክብሩ(both industry regulations and government legislations) ናቸው።"
    return adherence_to_standards


def medical_quality():
    st.info("16. የሕክምና ጥራት (Medical quality )")
    medical_quality = "ከክሊኒካል መተግበሪያው (WEB-APP) መሳሪያ ያገኘሁት የማስረጃ ጥራት ከፍተኛ እና ጠቃሚ ነው።"
    return medical_quality


def user_knowledge_and_skills():
    st.info("17. የተጠቃሚ እውቀት እና ችሎታ (User knowledge and skills )")
    Learnability = "የክሊኒካል መተግበሪያው (WEB-APP) የሚፈለጉትን ክሊኒካዊ ውጤቶች ያግዛል ወይም ይጨምራል እናም አሁን ካለው ሙያዊ እውቀት እና ችሎታ ጋር ይጣጣማል።"
    return Learnability


def usage():
    st.info("18. አጠቃቀም (Usage)")
    usage = "ከክሊኒካል መተግበሪያው (WEB-APP) ጋር ያለኝ ልምድ ምንም ችግር አላጋጠመውም።"
    return usage


def expectations_confirmation():
    st.info("19. የጠበቁትን ማረጋገጫ (Expectations confirmation)")
    expectations_confirmation = "በቀድሞ ልምዴ እና/ወይም በምጠብቀው ግዜ የክሊኒካል መተግበሪያውን እንደጠበቁት ሆኖ አግኝቼዋለሁ።"
    return expectations_confirmation


def satisfaction_of_over_quality():
    st.info("20. አጠቃላይ የጥራት ወይም ላቅ ያለ የጥሪት እርካታ (Satisfaction of over  quality)")
    satisfaction_of_over_quality = "በአጠቃላይ የክሊኒካል መተግበሪያው ስርዓት፣ አገልግሎት (ሪፈራል እና ሊታከሙ የሚችሉ ጉዳዮችን ለማግኘት  ለመለየት በሚያደርገው እና የመረጃ ጥረት) ተደስቻለሁ።"
    return satisfaction_of_over_quality


def overall_satisfaction():
    st.info("21. አጠቃላይ እርካታ  (Overall satisfaction)")
    overall_satisfaction = "በአጠቃላይ የክሊኒካል መተግበሪያው ስርዓት ተደስቻለሁ ማለትም የክሊኒካል መተግበሪያው ብጠቀም የማገኘዉን አገልግሎት ና ጥቅም  ተፅዕኖ እሪዳለሁ።"
    return overall_satisfaction


def intension_to_use():
    st.info("22. የመጠቀም ፍላጎት  (Intension to use)")
    intension_to_use = "የክሊኒካል መተግበሪያው ጥቅም ላይ ቢውል ስራዬን ለማከናወን ለመደበኛ ስራዬ የክሊኒካል መተግበሪያው ለመጠቀም አስባለሁ። ለተለመደ ተግባሬ የክሊኒካል መተግበሪያውን  ካገኘሁ እንደምቀበለው ተነብያለሁ።"
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
        evalutation_df == 'Neutral (ገለልተኛ)').stack().index.tolist()
    StronglyDisagreeResults = evalutation_df.where(
        evalutation_df == 'Strongly Disagree (በጣም አልስማማም)').stack().index.tolist()
    DisagreeResults = evalutation_df.where(
        evalutation_df == 'Disagree (አልስማማም)').stack().index.tolist()
    # rslt_Disagree = evalutation_df[evalutation_df[col] == 'Disagree (በጣም አልስማማም)']
    # rslt_neutral = evalutation_df[evalutation_df[col] == 'Neutral (ገለልተኛ)']
    st.write("Neutral (ገለልተኛ)", neutralResults)
    st.write("Strongly Disagree (በጣም አልስማማም)", StronglyDisagreeResults)
    st.write("Disagree ( አልስማማም)", DisagreeResults)


def main():
    """questionnairee web form"""
    st.info("የክሊኒካል መተግበሪያው (WEB-APP) ለመገምገም መጠይቁ የተዘጋጀው በ Ji, Mengting, et al. 2021 የምርምር ወረቀት ላይ ተመስርቶ ሲሆን ፧ በምርምር ፕሮቶኮላችን እና መስፈርቶቻችኅ መሰረት ተዘጋጅቶ የተሰደረ ነው::")
    st.success("እባክዎ የክሊኒካል መተግበሪያውን (WEB-APP) ከተጠቀሙ በኋላ መጠይቁን ይሙሉ")
    fullname = st.text_input('የገምጋሚ ሙሉ ስም (Evaluator Full Name)')

    evalutation_started_time = st.time_input('ግምገማው የጀመረበት ሰዓት (Evaluation started  time)')

    # timestamp = pd.Timestamp(datetime.today())
    # timestamp = datetime.datetime.now()
    # evalutation_started_time = st.write(
    # 'Evaluation started:', 'Hour:', timestamp.hour, 'Minute:', timestamp.minute, 'Second:', timestamp.second)

    reviewerResponseChoice = ['',
                              'በጣም ተስማምቻለው (Strongly Agree)',
                              'ተስማምቻለው (Agree)',
                              'ገለልተኛ (Neutral)',
                              'አልስማማም (Disagree)',
                              'በጣም አልስማማም (Strongly Disagree)',

                              # 'Comment in the case of neutral, disagree and strongly disagree (“ገለልተኛ፣ አልስማማም እና በጣም አልስማማም” በሚለው ጉዳይ ላይ አስተያየት ይስጡ)'
                              ]
    # making the orientaiton horizontal
    # st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    with st.expander(label="የክሊኒካል መተግበሪያው አጠቃቀም ቀላልነት(Perceived Ease of Use)"):
        learnability_Response = st.selectbox(learnability(), reviewerResponseChoice)
        operability_Response = st.selectbox(operability(), reviewerResponseChoice)
        user_interface_Response = st.selectbox(user_interface(), reviewerResponseChoice)
        data_entry_Response = st.selectbox(data_entry()+"\n", reviewerResponseChoice)
        advice_to_display_Response = st.selectbox(advice_to_display()+"\n", reviewerResponseChoice)
        legibility_Response = st.selectbox(legibility(), reviewerResponseChoice)

    with st.expander(label="የክሊኒካል መተግበሪያው ጥራት (System Quality)"):
        response_time_Response = st.selectbox(response_time(), reviewerResponseChoice)
        stability_Response = st.selectbox(stability(), reviewerResponseChoice)
    with st.expander(label="የመረጃ ጥራት(Information Quality ) "):
        security_Response = st.selectbox(security(), reviewerResponseChoice)
        cp_performance_Response = st.selectbox(cp_performance(), reviewerResponseChoice)

    with st.expander(label="የውሳኔ ለውጦች (Decision Changes) "):
        change_in_order_behavior_Response = st.selectbox(
            change_in_order_behavior(), reviewerResponseChoice)
        change_in_cp_Response = st.selectbox(change_in_cp(), reviewerResponseChoice)

    with st.expander(label="የሂደት ለውጦች (Process Changes)"):
        effectiveness_Response = st.selectbox(effectiveness(), reviewerResponseChoice)
        overall_usefulness_Response = st.selectbox(overall_usefulness(), reviewerResponseChoice)
        adherence_to_standards_Response = st.selectbox(
            adherence_to_standards(), reviewerResponseChoice)
        medical_quality_Response = st.selectbox(medical_quality(), reviewerResponseChoice)
        user_knowledge_and_skills_Response = st.selectbox(
            user_knowledge_and_skills(), reviewerResponseChoice)

    with st.expander(label="ተቀባይነት (Acceptance)"):
        usage_Response = st.selectbox(usage(), reviewerResponseChoice)
        expectations_confirmation_Response = st.selectbox(
            expectations_confirmation(), reviewerResponseChoice)
        satisfaction_of_over_quality_Response = st.selectbox(
            satisfaction_of_over_quality(), reviewerResponseChoice)
        overall_satisfaction_Response = st.selectbox(overall_satisfaction(), reviewerResponseChoice)
        intension_to_use_Response = st.selectbox(intension_to_use(), reviewerResponseChoice)
    evalutation_ended_time = st.time_input('ግምገማው ያለቀበት ሰዓት (Evaluation ends at)')

    with st.expander(label="Validate and Review the Response (ምላቮን አረጋግጠው ያፅድቁ)"):
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
