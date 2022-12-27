import streamlit as st

def album():
    st.set_page_config(page_title="#my_album", page_icon="🎑")
    st.markdown("album")
    st.sidebar.header("Albums inside")

    st.write("""
    demo
    """
    )