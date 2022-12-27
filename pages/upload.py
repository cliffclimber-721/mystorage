import streamlit as st
import datetime

st.set_page_config(page_title="my_upload", page_icon="📷")

uploadPhoto = st.file_uploader("Press to upload your memories 😆", accept_multiple_files=True, type="png")

if uploadPhoto:
    dateBtn = st.button("Your date?")
    if dateBtn:
        uploadDate = st.date_input("Date input", datetime.date(2022, 12, 1))
