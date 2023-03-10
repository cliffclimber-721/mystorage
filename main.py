import streamlit as st
import streamlit_authenticator as stauth
import yaml

st.set_page_config(
    page_title="#my_storage",
    page_icon="π·"
)

st.markdown("""
### #my_storage μμ κ°λ¨ν μ¨λ²μ λ§λ€μ΄λ³Ό μ μμ΄μβοΈ
**π λ©λ΄λ ν¨κ» μ°Έκ³ ν΄μ£ΌμΈμβοΈ**
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