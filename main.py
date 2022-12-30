import streamlit as st
import streamlit_authenticator as stauth
import yaml

st.set_page_config(
    page_title="#my_storage",
    page_icon="📷"
)

st.markdown("""
### #my_storage 에서 간단한 앨범을 만들어볼 수 있어요❗️
**👈 메뉴도 함께 참고해주세요❗️**
""")

hashpwd = stauth.Hasher(['0721', '0123']).generate

with open("/Users/skywalker721/Desktop/github_file/mystorage/config.yaml") as file:
    config = yaml.load(file, Loader=yaml.Loader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')