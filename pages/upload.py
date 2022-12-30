import streamlit as st
import datetime

st.title("#my_storage")
photoBtn = st.button("Press to upload❗️")
uploadPhoto = st.file_uploader("Press to upload your memories 😆", accept_multiple_files=True, type="png")
defaultDate = datetime.date(2015, 1, 1)

if photoBtn:
    uploadPhoto
    if uploadPhoto:
        with st.form("my_form"):
            st.write("Please select your date")
            uploadDate = st.date_input("Date input", value=defaultDate)
            submitted = st.form_submit_button("Submit")

            if submitted:
                if uploadDate == defaultDate:
                    st.write("Date not changed, Please select your date.")
                else:
                    st.write("Date changed. Write your code below what you want.")